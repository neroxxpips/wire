# pylint: disable=duplicate-code
"""
    AnchorDataImporter
    ============
    .. Copyright:
        Copyright Wirepas Ltd 2021 licensed under Apache License, Version 2.0
        See file LICENSE for full license details.

    Imports data from JSON file to WNT 4.0 backend
"""
from utils import get_settings, setup_log
from connections import Connections
from exitcode import ExitCode
from websocket import WebSocketException

import time
import json
import sys
from enum import Enum, auto
from nodemessages import NodeMessages

SETTINGS_PREFIX = "import_environment"


class Messages(NodeMessages):
    """Aggregation class for messages"""

    def __init__(self, logger, protocol_version) -> None:
        """Initialization

        Args:
            logger (Logger): logger
            protocol_version (int): protocol version of authentication and metadata connection
        """
        NodeMessages.__init__(self, logger, protocol_version)


class AnchorDataImporter(object):
    """Main example class which is run"""

    class State(Enum):
        """State enumeration class"""

        START = auto()
        LOGIN = auto()  # Started on authentication_on_open
        SET_NODE_METADATA = auto()
        END = auto()

    def __init__(self) -> None:
        """Initialization"""
        try:
            self.settings = get_settings(SETTINGS_PREFIX)

            self.logger = setup_log("MetadataUpdater", self.settings.log_level, self.settings.log_file_name)
            self.logger.info("Starting import")

            self.import_data = None
            self.return_code = ExitCode.STARTED
            self.state = self.State(self.State.START.value + 1)

            self.authentication_thread = None
            self.metadata_thread = None

            self.client = Connections(
                hostname=self.settings.hostname,
                logger=self.logger,
                authentication_on_open=self.authentication_on_open,
                authentication_on_message=self.authentication_on_message,
                authentication_on_error=self.authentication_on_error,
                authentication_on_close=self.authentication_on_close,
                metadata_on_open=self.metadata_on_open,
                metadata_on_message=self.metadata_on_message,
                metadata_on_error=self.metadata_on_error,
                metadata_on_close=self.metadata_on_close,
                settings_prefix=SETTINGS_PREFIX
            )

            self.messages = Messages(self.logger, self.settings.protocol_version)
        except Exception as e:
            print(f"Something went really wrong during initializing: {e}")
            raise e

    def set_return_code(self, code: ExitCode):
        if self.return_code == ExitCode.STARTED:
            self.return_code = code

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
        elif self.state == self.State.SET_NODE_METADATA:
            if not self.import_data or (self.import_data and len(self.import_data) == 0):
                self.state = self.State.END
            else:
                data_batch = self.import_data[:self.settings.batch_size]
                del self.import_data[:self.settings.batch_size]

                self.logger.debug(f"unprocessed: {len(self.import_data)}")
                time.sleep(self.settings.batch_delay_seconds)
                node_data = []
                for node in data_batch:
                    node_data.append({
                        "id": node['id'],
                        "network_id": node['network_id'],
                        "is_anchor": node['is_anchor'],
                        "is_approved": True,
                    })

                message = json.dumps(
                    self.messages.message_set_nodes_metadata(
                        nodes=node_data
                    )
                )
                self.logger.info(f"sent message {str(message)}")
                self.metadata_thread.socket.send(message)

    def parse_response(self, message: str) -> ExitCode:
        """Parse response

        Args:
            message (str): received message

        Returns:
            bool: None if response's request succeeded, ExitCode for the script if failed
        """
        if self.state == self.State.LOGIN and not self.messages.parse_login((json.loads(message))):
            return ExitCode.LOGIN_FAILED
        elif self.state == self.State.SET_NODE_METADATA and not self.messages.parse_set_node_metadata(json.loads(message)):
            return ExitCode.SET_ANCHOR_FAILED
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
            self.logger.info("auth_on_error")
            if websocket.keep_running:
                self.logger.error("Authentication socket error: {0}".format(error))
            self.set_return_code(ExitCode.WEBSOCKET_ERROR)
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
            self.stop_connection_threads(ExitCode.UNDEFINED_EXCEPTION)

    def metadata_on_open(self, _websocket) -> None:
        """Websocket callback when the metadata websocket has been opened

        Args:
            websocket (Websocket): communication socket
        """
        try:
            self.logger.info("Metadata socket open")
        except WebSocketException as e:
            self.logger.error(e)
            self.stop_connection_threads(ExitCode.WEBSOCKET_ERROR)
        except Exception as e:
            self.logger.error(f"exception {sys.exc_info()[0]} occurred")
            self.logger.error(e)
            self.stop_connection_threads(ExitCode.UNDEFINED_EXCEPTION)

    def metadata_on_message(self, websocket, message: str) -> None:
        """Websocket callback when a new metadata message arrives

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

    def metadata_on_error(self, websocket, error: str) -> None:
        """Websocket callback when a metadata socket error occurs

        Args:
            websocket (Websocket): communication socket
            error (str): error message
        """
        try:
            if websocket.keep_running:
                self.logger.error("Metadata socket error: {0}".format(error))
            self.set_return_code(ExitCode.WEBSOCKET_ERROR)
        except WebSocketException as e:
            self.logger.error(e)
            self.stop_connection_threads(ExitCode.WEBSOCKET_ERROR)
        except Exception as e:
            self.logger.error(f"exception {sys.exc_info()[0]} occurred")
            self.logger.error(e)
            self.stop_connection_threads(ExitCode.UNDEFINED_EXCEPTION)

    def metadata_on_close(self, _websocket) -> None:
        """Websocket callback when the metadata connection closes

        Args:
            _websocket (Websocket): communication socket
        """
        try:
            self.logger.warning("Metadata socket close")
        except WebSocketException as e:
            self.logger.error(e)
            self.stop_connection_threads(ExitCode.WEBSOCKET_ERROR)
        except Exception as e:
            self.logger.error(f"exception {sys.exc_info()[0]} occurred")
            self.logger.error(e)
            self.stop_connection_threads(ExitCode.UNDEFINED_EXCEPTION)

    def on_message(self, _websocket, message: str) -> None:
        """Called when authentication or metadata message is received

        Handles the state machine and closing of the communication threads

        Args:
            websocket (Websocket): communication socket
            message (str): received message
        """
        parse = self.parse_response(message)
        if parse is not None:
            self.logger.error("Run failed. Exiting.")
            self.stop_connections(parse)
        else:
            if self.state.value < self.State.SET_NODE_METADATA.value:
                self.state = self.State(self.state.value + 1)
            if self.state == self.State.SET_NODE_METADATA:
                if len(self.import_data) == 0:
                    self.state = self.State(self.state.value + 1)
                else:
                    self.send_request()
            if self.state == self.State.END:
                self.stop_connections(ExitCode.SUCCESS)

    def stop_connections(self, return_code: ExitCode = ExitCode.SUCCESS) -> None:
        """Closes connections and sets return code
        :param return_code: ExitCode defaults to success
        :return: None
        """
        self.set_return_code(return_code)
        self.client.stop_metadata_thread()
        self.client.stop_authentication_thread()

    def run(self) -> int:
        """Run method which starts and waits the communication thread(s)

        Returns:
            int: Process return code
        """
        try:
            # Read import data from file to memory
            data_file = open(self.settings.data_file_name, "r")
            self.import_data = json.load(data_file)
            data_amount = len(self.import_data)
            data_file.close()

            # Start threads
            self.authentication_thread = self.client.start_authentication_thread()
            self.metadata_thread = self.client.start_metadata_thread()

            self.metadata_thread.join(self.settings.timeout_minutes * 60)
            self.authentication_thread.join(self.settings.timeout_minutes * 60)

            if (self.return_code == ExitCode.STARTED or self.return_code == ExitCode.SUCCESS) \
                    and len(self.import_data) != 0:
                # return_code is not set or success, but still data to process
                self.logger.error(f"Amount of unprocessed data from JSON: {len(self.import_data)}")
                self.return_code = ExitCode.UNPROCESSED_DATA

            self.logger.info(f"Successful import for {data_amount} anchors")
            self.set_return_code(ExitCode.SUCCESS)

        except WebSocketException as e:
            self.logger.error(e)
            self.set_return_code(ExitCode.WEBSOCKET_ERROR)
            pass
        except FileNotFoundError:
            self.set_return_code(ExitCode.DATA_MISSING)
            pass
        except Exception as e:
            self.logger.error(e)
            self.set_return_code(ExitCode.UNDEFINED_EXCEPTION)
            pass

        return self.return_code.value


if __name__ == "__main__":
    try:
        anchordataimporter = AnchorDataImporter()
        rc = anchordataimporter.run()
        exit(rc)
    except Exception as e:
        exit(ExitCode.UNDEFINED_EXCEPTION)
