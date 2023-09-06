# pylint: disable=duplicate-code
"""
    AnchorDataExporter
    =====================
    .. Copyright:
        Copyright Wirepas Ltd 2021 licensed under Apache License, Version 2.0
        See file LICENSE for full license details.

    Exports data from WNT 3.0 backend to a file defined in settings.yml
"""
import threading
from copy import copy
from typing import Optional

from migrationdata import MigrationData, MigrationDataJsonEncoder
from utils import get_settings, setup_log
from exitcode import ExitCode
from connections import Connections
from websocket import WebSocketException

import json
import os
import sys
import wirepas_messaging.wnt as wnt_proto

from enum import Enum, auto

from wirepas_messaging.wnt.ws_api import RealtimeSituationMessages

SETTINGS_PREFIX = "export_environment"


class AnchorDataExporter(object):
    """Main example class which is run"""

    class State(Enum):
        """State enumeration class"""

        START = auto()

        LOGIN = auto()  # Started on authentication_on_open
        REALTIME_SITUATION_LOGIN = auto()

        WAIT_FOR_STARTUP_SITUATION = auto()
        WAIT_FOREVER = auto()

        END = auto()

    def __init__(self) -> None:
        """Initialization"""
        try:
            self.settings = get_settings(SETTINGS_PREFIX)
            self.logger = setup_log("RealtimeDataExporter", self.settings.log_level, self.settings.log_file_name)
            self.logger.info("Starting export")

            self.return_code = ExitCode.STARTED
            self.state = self.State(self.State.START.value + 1)

            self.authentication_thread = None
            self.realtime_situation_thread = None
            self.check_status_thread = None

            self.distinct_cluster_nodes = []
            self.cluster_size = 0
            self.distinct_nodes = []
            self.partial_nodes = 0
            self.total_node_count = 0
            self.export_data = []

            self.previous_state = None

            self.client = Connections(
                hostname=self.settings.hostname,
                logger=self.logger,
                authentication_on_open=self.authentication_on_open,
                authentication_on_message=self.authentication_on_message,
                authentication_on_error=self.authentication_on_error,
                authentication_on_close=self.authentication_on_close,
                realtime_situation_on_open=self.realtime_situation_on_open,
                realtime_situation_on_message=self.realtime_situation_on_message,
                realtime_situation_on_error=self.realtime_situation_on_error,
                realtime_situation_on_close=self.realtime_situation_on_close,
                settings_prefix=SETTINGS_PREFIX,
            )

            self.messages = RealtimeSituationMessages(
                self.logger, self.settings.protocol_version
            )
        except Exception as e:
            print(f"Something went really wrong during initializing: {e}")
            raise e

    def set_return_code(self, code: ExitCode):
        if self.return_code == ExitCode.STARTED:
            self.return_code = code

    def get_node_count(self):
        return self.partial_nodes + len(self.distinct_nodes)

    def check_status(self, timeout: int) -> threading.Timer:
        self.logger.debug("Check status")
        # TOCTOU is not a problem here, since state always increments and is eventually correct
        if self.previous_state is not None \
                and (len(self.previous_state['distinct_nodes'])
                     + self.previous_state['missing_nodes']) == self.get_node_count() \
                and self.get_node_count() != self.total_node_count:
            self.stop_connection_threads(ExitCode.RECEIVE_DATA_TIMEOUT)
        else:
            self.previous_state = {
                "distinct_nodes": copy(self.distinct_nodes),
                "missing_nodes": copy(self.partial_nodes),
                "distinct_cluster_nodes": copy(self.distinct_cluster_nodes),
                "cluster_size": copy(self.cluster_size),
                "total_node_count": copy(self.total_node_count)
            }
            if self.return_code == ExitCode.STARTED:
                self.check_status_thread = threading.Timer(timeout, self.check_status, [timeout])
                self.check_status_thread.start()
        return self.check_status_thread

    def send_request(self) -> None:
        """Send request"""
        if self.state == self.State.LOGIN:
            self.authentication_thread.socket.send(
                json.dumps(
                    self.messages.message_login(
                        self.settings.username, self.settings.password
                    )
                )
            )

        elif self.state == self.State.REALTIME_SITUATION_LOGIN:
            self.realtime_situation_thread.socket.send(
                json.dumps(
                    self.messages.message_realtime_situation_login(
                        self.messages.session_id
                    )
                )
            )

    def parse_response(self, message: str) -> Optional[ExitCode]:
        """Parse response
        Args:
            message (str): received message
        Returns:
            bool: None if response's request succeeded, ExitCode for the script if failed
        """
        if self.state == self.State.LOGIN and not self.messages.parse_login(json.loads(message)):
            return ExitCode.LOGIN_FAILED
        if self.state == self.State.REALTIME_SITUATION_LOGIN \
                and not self.messages.parse_realtime_situation_login(json.loads(message)):
            return ExitCode.RTSITUATION_LOGIN_FAILED
        return None

    def authentication_on_open(self, _websocket) -> None:
        """Websocket callback when the authentication websocket has been opened
        Args:
            websocket (Websocket): communication socket
        """
        try:
            self.logger.info("Authentication socket open")
            self.send_request()
        except WebSocketException as e:
            self.logger.error(e)
            self.stop_connection_threads(ExitCode.WEBSOCKET_ERROR)
        except Exception as e:
            self.logger.error(f"exception {sys.exc_info()[0]} occurred")
            self.logger.error(e)
            self.stop_connection_threads(ExitCode.UNDEFINED_EXCEPTION)

    def authentication_on_message(self, websocket, message: str) -> None:
        """Websocket callback when a new authentication message arrives
        Args:
            websocket (Websocket): communication socket
            message (str): received message
        """
        try:
            self.on_message(websocket, message)
        except WebSocketException as e:
            self.logger.error(e)
            self.stop_connection_threads(ExitCode.WEBSOCKET_ERROR)
        except Exception as e:
            self.logger.error(f"exception {sys.exc_info()[0]} occurred")
            self.logger.error(e)
            self.stop_connection_threads(ExitCode.UNDEFINED_EXCEPTION)

    def authentication_on_error(self, websocket, error: str) -> None:
        """Websocket callback when an authentication socket error occurs
        Args:
            websocket (Websocket): communication socket
            error (str): error message
        """
        try:
            if websocket.keep_running:
                self.logger.error("Authentication socket error: {0}".format(error))
            self.stop_connection_threads(ExitCode.WEBSOCKET_ERROR)
        except WebSocketException as e:
            self.logger.error(e)
            self.stop_connection_threads(ExitCode.WEBSOCKET_ERROR)
        except Exception as e:
            self.logger.error(f"exception {sys.exc_info()[0]} occurred")
            self.logger.error(e)
            self.stop_connection_threads(ExitCode.UNDEFINED_EXCEPTION)

    def authentication_on_close(self, _websocket) -> None:
        """Websocket callback when the authentication connection closes
        Args:
            _websocket (Websocket): communication socket
        """
        try:
            self.logger.info("Authentication socket close")
        except WebSocketException as e:
            self.logger.error(e)
            self.stop_connection_threads(ExitCode.WEBSOCKET_ERROR)
        except Exception as e:
            self.logger.error(f"exception {sys.exc_info()[0]} occurred")
            self.logger.error(e)

    def realtime_situation_on_open(self, _websocket) -> None:
        """Websocket callback when the realtime situation websocket has been opened
        Args:
            websocket (Websocket): communication socket
        """
        try:
            self.logger.info("Realtime situation socket open")
        except WebSocketException as e:
            self.logger.error(e)
            self.stop_connection_threads(ExitCode.WEBSOCKET_ERROR)
        except Exception as e:
            self.logger.error(f"exception {sys.exc_info()[0]} occurred")
            self.logger.error(e)
            self.stop_connection_threads(ExitCode.UNDEFINED_EXCEPTION)

    def realtime_situation_on_message(self, websocket, message: str) -> None:
        """Websocket callback when a new realtime situation message arrives
        Args:
            websocket (Websocket): communication socket
            message (str): received message
        """
        try:
            self.on_message(websocket, message)
        except WebSocketException as e:
            self.logger.error(e)
            self.stop_connection_threads(ExitCode.WEBSOCKET_ERROR)
        except Exception as e:
            self.logger.error(f"exception {sys.exc_info()[0]} occurred")
            self.logger.error(e)
            self.stop_connection_threads(ExitCode.UNDEFINED_EXCEPTION)

    def realtime_situation_on_error(self, websocket, error: str) -> None:
        """Websocket callback when realtime situation socket error occurs
        Args:
            websocket (Websocket): communication socket
            error (str): error message
        """
        try:
            if websocket.keep_running:
                self.logger.error("Realtime situation socket error: {0}".format(error))
            self.set_return_code(ExitCode.WEBSOCKET_ERROR)
        except WebSocketException as e:
            self.logger.error(e)
            self.stop_connection_threads(ExitCode.WEBSOCKET_ERROR)
        except Exception as e:
            self.logger.error(f"exception {sys.exc_info()[0]} occurred")
            self.logger.error(e)
            self.stop_connection_threads(ExitCode.UNDEFINED_EXCEPTION)

    def realtime_situation_on_close(self, _websocket) -> None:
        """Websocket callback when the realtime situation connection closes
        Args:
            _websocket (Websocket): communication socket
        """
        try:
            self.logger.warning("Realtime situation socket close")
        except WebSocketException as e:
            self.logger.error(e)
            self.stop_connection_threads(ExitCode.WEBSOCKET_ERROR)
        except Exception as e:
            self.logger.error(f"exception {sys.exc_info()[0]} occurred")
            self.logger.error(e)
            self.stop_connection_threads(ExitCode.UNDEFINED_EXCEPTION)

    def on_message(self, _websocket, message: str) -> None:
        """Called when authentication message is received
        Handles the state machine and closing of the communication threads
        Args:
            websocket (Websocket): communication socket
            message (str): received message
        """
        if self.state.value < self.State.WAIT_FOR_STARTUP_SITUATION.value:  # start, login, realtime_situation_login
            self.start_login_realtime_situation_login_state_message(message)
            return

        if self.state == self.state.WAIT_FOR_STARTUP_SITUATION:
            self.wait_for_startup_situation_state_message(message)

        if self.state == self.state.WAIT_FOREVER:
            # no need to wait forever, leave this here for possible future needs
            self.state = self.State(self.state.value + 1)

        if self.state == self.state.END:
            self.handle_end_state()

    def start_login_realtime_situation_login_state_message(self, message: str) -> None:
        """Process message in states of START, LOGIN, REALTIME_SITUATION_LOGIN
        Args:
            message(str): unparsed message
        Returns: None
        """
        parse = self.parse_response(message)
        if parse is not None:
            self.logger.error("Run failed. Exiting.")
            self.stop_connection_threads(parse)
        else:
            # successful auth login or rtsituation login, continue to next state
            self.state = self.State(self.state.value + 1)
            self.send_request()

    def wait_for_startup_situation_state_message(self, message: str) -> None:
        """Process message in state of WAIT_FOR_STARTUP_SITUATION
        Args:
            message(str): unparsed message from the backend
        returns:
            None
        """
        wnt_message = wnt_proto.Message()
        wnt_message.ParseFromString(message)
        # Process message, depending on different conditions.
        if self.rtsituation_metadata_initial_message(wnt_message):
            self.logger.debug("Processed rtsituation initial message")
        elif self.rtsituation_ignore_message(wnt_message):
            self.logger.debug("Do nothing, and skip rest of elseifs - Some other than node update message")
        #  Rest should be related to node updates
        elif self.process_update_node_message(wnt_message):
            self.logger.debug(f"processed node update message (Full or Delta) with "
                              f"node id {wnt_message.source_address} from network {wnt_message.network_id}")
        elif self.process_partial_node_message(wnt_message):
            self.logger.debug("Processed partial node message")

        # At the end, check that if state should be incremented to END
        if self.cluster_size != 0 \
                and self.get_node_count() == self.total_node_count \
                and len(self.distinct_cluster_nodes) == self.cluster_size:
            # Initial nodes' data loaded and got total node count from all rtsituations
            self.logger.info("Startup situation received from all rtsituation managers")
            self.state = self.State(self.state.value + 1)

    def rtsituation_metadata_initial_message(self, wnt_message: wnt_proto.Message) -> bool:
        """Processes rtsituation initial cluster message
        Args:
            wnt_message(wnt_proto.Message): parsed message
        Returns:
            True if message is rtsituation metadata message with cluster and total node count information
            False otherwise
        """
        if wnt_message.HasField("rtsituation_metadata") \
                and wnt_message.rtsituation_metadata.HasField("node_count") \
                and wnt_message.rtsituation_metadata.HasField("cluster_no") \
                and wnt_message.rtsituation_metadata.HasField("cluster_size") \
                and wnt_message.rtsituation_metadata.cluster_no not in self.distinct_cluster_nodes:
            self.logger.info(f"Got node count {wnt_message.rtsituation_metadata.node_count} from rtsituation id "
                             f"{wnt_message.rtsituation_metadata.cluster_no} "
                             f"of cluster size "
                             f"{wnt_message.rtsituation_metadata.cluster_size}")
            self.total_node_count += wnt_message.rtsituation_metadata.node_count
            self.distinct_cluster_nodes.append(wnt_message.rtsituation_metadata.cluster_no)
            self.cluster_size = wnt_message.rtsituation_metadata.cluster_size
            return True
        return False

    def rtsituation_ignore_message(self, wnt_message: wnt_proto.Message) -> bool:
        """Handles message types which are skipped in this migration script context
        Args:
            wnt_message(wnt_proto.Message): parsed message
        Returns:
            True if message is type which should be ignored and should not be processed further
            False otherwise
        """
        return wnt_message.HasField("positioning_status_data") \
               or wnt_message.HasField("backend_heartbeat") \
               or (wnt_message.HasField("node_metadata") \
                   and wnt_message.node_metadata.HasField("is_deleted") \
                   and wnt_message.node_metadata.is_deleted) \
               or wnt_message.HasField("metadata_update_message") \
               or wnt_message.HasField("gateway_info") \
               or wnt_message.HasField("backend_component_info")

    def process_update_node_message(self, wnt_message: wnt_proto.Message):
        """Processes rtsituation messages with initial node data (Full) or change data (Delta)
        Args:
            wnt_message(wnt_proto.Message): parsed message
        Returns:
            True if message was processed
            False otherwise
        """
        if wnt_message.HasField("source_address") \
                and wnt_message.HasField("network_id") \
                and wnt_message.HasField("backend_message") \
                and wnt_message.backend_message.HasField("message"):
            if wnt_message.backend_message.message == wnt_message.backend_message.Full \
                    and wnt_message.source_address not in self.distinct_nodes:
                # This is Full message with necessary data to save distinct node
                self.distinct_nodes.append((wnt_message.network_id, wnt_message.source_address))
                if self.get_node_count() % 1000 == 0:
                    self.logger.debug(f"processed {self.get_node_count()} nodes and "
                                      f"{len(self.export_data)} anchors")
                if wnt_message.source_address != 0:  # Do not export node with source_address 0
                    migration_data = MigrationData(wnt_message)
                    if migration_data.is_anchor:
                        self.export_data.append(migration_data)

            elif wnt_message.backend_message.message == wnt_message.backend_message.Delta:
                # Delta message of some node
                self.logger.debug(str(wnt_message))
            return True
        return False

    def process_partial_node_message(self, wnt_message: wnt_proto.Message) -> bool:
        """Processes partial node information messages
        Args:
            wnt_message(wnt_proto.Message): parsed message
        Returns:
            True if messages was processed
            False otherwise
        """
        if not wnt_message.HasField("source_address") \
                or wnt_message.source_address == 0 \
                or wnt_message.HasField("network_id") \
                or wnt_message.network_id == 0:
            # some odd state in which I should count as node in total_nodes.
            self.partial_nodes += 1
            return True
        return False

    def handle_end_state(self) -> None:
        """Handle end state
        Args: None
        Returns: None
        """
        if len(self.export_data) == 0:
            self.logger.error("No data received, and therefore no data exported")
            self.stop_connection_threads(ExitCode.DATA_MISSING)
        else:
            with open(self.settings.data_file_name, "a+", encoding="utf8") as file:
                json.dump(self.export_data, file, indent=2, cls=MigrationDataJsonEncoder)
            self.stop_connection_threads(ExitCode.SUCCESS)

    def stop_connection_threads(self, exit_code: ExitCode) -> None:
        """Stop all connection threads"""
        self.logger.info(f"stop_connections with exit_code {exit_code}")
        self.set_return_code(exit_code)
        try:
            self.check_status_thread.cancel()
            self.client.stop_realtime_situation_thread()
            self.client.stop_authentication_thread()
        except (WebSocketException, AttributeError) as e:
            # Usually connections are already closed
            pass

    def run(self) -> int:
        """Run method which starts and waits the communication thread(s)
        Returns:
            int: Process return code
        """
        try:
            # Remove data.json if it exists. Script will rewrite it.
            if self.settings.data_file_name and os.path.exists(self.settings.data_file_name):
                os.remove(self.settings.data_file_name)

            self.realtime_situation_thread = self.client.start_realtime_situation_thread()
            self.authentication_thread = self.client.start_authentication_thread()
            self.check_status_thread = self.check_status(60)

            self.realtime_situation_thread.join(self.settings.timeout_minutes * 60)
            self.authentication_thread.join(self.settings.timeout_minutes * 60)
            self.check_status_thread.cancel()

            if (self.return_code == ExitCode.SUCCESS or self.return_code == ExitCode.STARTED) \
                    and (self.get_node_count() != self.total_node_count \
                         or len(self.distinct_cluster_nodes) != self.cluster_size):
                self.logger.error(f"Connection closed before all initial data received ("
                                  f"cluster nodes ({self.distinct_cluster_nodes} of cluster size {self.cluster_size}) "
                                  f"nodes ({self.get_node_count()}/{self.total_node_count}")
                self.return_code = ExitCode.INITIAL_DATA_FAILURE

            if self.return_code == ExitCode.STARTED or self.return_code == ExitCode.SUCCESS:
                self.return_code = ExitCode.SUCCESS
                self.logger.info(f"Succesfully saved state of "
                                 f"cluster nodes ({self.distinct_cluster_nodes} of cluster size {self.cluster_size}) "
                                 f"nodes ({self.get_node_count()}/{self.total_node_count}) "
                                 f"anchor nodes ({len(self.export_data)})")
            else:
                self.logger.info(f"Failing with exit_code {self.return_code} and state "
                                 f"cluster nodes ({self.distinct_cluster_nodes} of cluster size {self.cluster_size}) "
                                 f"nodes ({self.get_node_count()}/{self.total_node_count})")

        except WebSocketException as e:
            self.logger.error(e)
            self.set_return_code(ExitCode.WEBSOCKET_ERROR)
        except Exception as e:
            self.logger.error(f"exception {sys.exc_info()[0]} occurred")
            self.logger.error(e)
            self.set_return_code(ExitCode.UNDEFINED_EXCEPTION)

        return self.return_code.value


if __name__ == "__main__":
    try:
        ae = AnchorDataExporter()
        rc = ae.run()
        exit(rc)
    except Exception as e:
        exit(ExitCode.UNDEFINED_EXCEPTION)

