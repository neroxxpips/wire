# pylint: disable=duplicate-code
"""
    Networks
    ========

    Network related metadata connection messages

"""
from .authenticationmessages import AuthenticationMessages


class NetworkMessages(AuthenticationMessages):
    """This class generates and decodes network related metadata connection messages"""

    def __init__(self, logger, protocol_version):
        """Initialization

        Args:
            logger (Logger): logger
            protocol_version (int): protocol version of authentication and metadata connection
        """
        super(NetworkMessages, self).__init__(logger, protocol_version)

    def message_create_network(self, network_id: str, network_name: str) -> dict:
        """Returns network creation message, which is used to bind name to network id

        Args:
            network_id (str): network id
            network_name (str): network name
        """
        message = dict(
            version=self.protocol_version,
            session_id=self.session_id,
            type=AuthenticationMessages.MessageTypes.CREATE_NETWORK.value,
            data=dict(
                networks=[dict(id=network_id, name=network_name)],
                originator_token=self.originator_token,
            ),
        )

        self.logger.info(self.json_dump_pretty(message))
        return message

    def parse_create_network(self, message: dict) -> bool:
        """Parses create network response

        Args:
            message (dict): the create network response

        Returns:
            bool: True if message validation succeeded, else False
        """
        try:
            self.validate(message)
            self.logger.info(self.json_dump_pretty(message))
        except ValueError:
            self.logger.error("Cannot create network")
            self.logger.error(self.json_dump_pretty(message))
            return False

        return True

    def message_update_network(self, network_id: str, network_name: str) -> dict:
        """Returns network update message

        Args:
            network_id (str): network id
            network_name (str): network name
        """
        message = dict(
            version=self.protocol_version,
            session_id=self.session_id,
            type=AuthenticationMessages.MessageTypes.UPDATE_NETWORK.value,
            data=dict(
                networks=[dict(id=network_id, name=network_name)],
                originator_token=self.originator_token,
            ),
        )

        self.logger.info(self.json_dump_pretty(message))
        return message

    def parse_update_network(self, message: dict) -> bool:
        """Parses update network response

        Args:
            message (dict): the update network response

        Returns:
            bool: True if message validation succeeded, else False
        """
        try:
            self.validate(message)
            self.logger.info(self.json_dump_pretty(message))
        except ValueError:
            self.logger.error("Cannot update network")
            self.logger.error(self.json_dump_pretty(message))
            return False

        return True

    def message_get_networks(self) -> dict:
        """Returns get networks message"""
        message = dict(
            version=self.protocol_version,
            session_id=self.session_id,
            type=AuthenticationMessages.MessageTypes.GET_NETWORKS.value,
            data=dict(originator_token=self.originator_token),
        )

        self.logger.info(self.json_dump_pretty(message))
        return message

    def parse_get_networks(self, message: dict) -> bool:
        """Parses get networks response

        Args:
            message (dict): the get networks response

        Returns:
            bool: True if message validation succeeded, else False
        """
        try:
            self.validate(message)
            self.logger.info(self.json_dump_pretty(message))
        except ValueError:
            self.logger.error("Cannot delete network")
            self.logger.error(self.json_dump_pretty(message))
            return False

        return True

    def message_delete_network(self, network_id: str) -> dict:
        """Returns network delete message

        Args:
            network_id (str): network id
        """
        message = dict(
            version=self.protocol_version,
            session_id=self.session_id,
            type=AuthenticationMessages.MessageTypes.DELETE_NETWORK.value,
            data=dict(
                networks=[dict(id=network_id)], originator_token=self.originator_token
            ),
        )

        self.logger.info(self.json_dump_pretty(message))
        return message

    def parse_delete_network(self, message: dict) -> bool:
        """Parses delete network response

        Args:
            message (dict): the delete network response

        Returns:
            bool: True if message validation succeeded, else False
        """
        try:
            self.validate(message)
            self.logger.info(self.json_dump_pretty(message))
        except ValueError:
            self.logger.error("Cannot delete network")
            self.logger.error(self.json_dump_pretty(message))
            return False

        return True
