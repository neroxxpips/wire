# pylint: disable=duplicate-code
"""
    Nodes
    =====

    Node related metadata connection messages needed to migrate anchor data from 3.0 to 4.0
"""
from typing import Dict, Any, List

from wirepas_messaging.wnt.ws_api.authenticationmessages import AuthenticationMessages


class NodeMessages(AuthenticationMessages):
    """This class generates and decodes node related metadata connection messages"""

    def __init__(self, logger, protocol_version) -> None:
        """Initialization

        Args:
            logger: logger
            protocol_version: protocol version of authentication and metadata connection
        """
        super(NodeMessages, self).__init__(logger, protocol_version)

    def message_set_nodes_metadata(
            self,
            nodes: List[dict],
    ) -> dict:
        """Returns set multiple nodes metadata message

        Args:
            nodes: list of nodes metadata
        """
        message = dict(
            version=self.protocol_version,
            session_id=self.session_id,
            type=AuthenticationMessages.MessageTypes.SET_NODE_METADATA.value,
            data=dict(
                nodes=nodes,
                originator_token=self.originator_token,
            ),
        )

        self.logger.debug(self.json_dump_pretty(message))
        return message

    def parse_set_node_metadata(self, message: Dict[str, Any]) -> bool:
        """Parses set node metadata response

        Args:
            message: set node metadata response

        Returns:
            bool: True if message validation succeeded, else False
        """
        try:
            self.validate(message)
            self.logger.info(self.json_dump_pretty(message))
        except ValueError:
            self.logger.error("Cannot set node metadata")
            self.logger.error(self.json_dump_pretty(message))
            return False

        return True
