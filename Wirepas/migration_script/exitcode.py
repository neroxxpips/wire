from enum import Enum, auto


class ExitCode(Enum):
    """ExitCode enumeration class"""
    STARTED = -1  # This should never actually be exited with
    SUCCESS = 0
    UNDEFINED_EXCEPTION = 1
    LOGIN_FAILED = 2
    SET_ANCHOR_FAILED = 3
    RTSITUATION_LOGIN_FAILED = 4
    INITIAL_DATA_FAILURE = 5
    DATA_MISSING = 6
    UNPROCESSED_DATA = 7
    WEBSOCKET_ERROR = 8
    RECEIVE_DATA_TIMEOUT = 9
