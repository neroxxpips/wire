import uuid
import os

PROTOCOL_VERSION = 4

RESULT_FIELD = "result"
DATA_FIELD = "data"
SESSION_ID_FIELD = "session_id"
TYPE_FIELD = "type"
VERSION_FIELD = "version"
USERNAME_FIELD = "username"
PASSWORD_FIELD = "password"
ORIGINATOR_TOKEN_FIELD = "originator_token"
USERS_FIELD = "users"
FULLNAME_FIELD = "full_name"
ROLE_FIELD = "role"
BUILDINGS_FIELD = "buildings"
NAME_FIELD = "name"
ID_FIELD = "id"
FLOOR_PLANS_FIELD = "floor_plans"
LEVEL_FIELD = "level"
IMAGE_ID_FIELD = "image_id"
IMAGE_THUMBNAIL_ID_FIELD = "image_thumbnail_id"
IMAGE_WIDTH_FIELD = "image_width"
IMAGE_HEIGHT_FIELD = "image_height"
IMAGE_BASE64_FIELD = "image_base64"
AREAS_FIELD = "areas"
LLAS_FIELD = "llas"
ALTITUDE_FIELD = "altitude"
LATITUDE_FIELD = "latitude"
LONGITUDE_FIELD = "longitude"
NETWORKS_FIELD = "networks"
NODES_FIELD = "nodes"
FLOOR_PLAN_ID_FIELD = "floor_plan_id"
NETWORK_ID_FIELD = "network_id"
DESCRIPTION_FIELD = "description"
IS_APPROVED_FIELD = "is_approved"
IS_VIRTUAL_FIELD = "is_virtual"
IS_SINK_FIELD = "is_sink"
APPLICATION_DATA_FIELD = "application_data"
DIAGNOSTICS_INTERVAL_FIELD = "diagnostics_interval"
IS_OVERRIDE_ON_FIELD = "is_override_on"
SINKS_NODE_IDS_FIELD = "sink_node_ids"
COMMAND_FIELD = "command"
NODE_ID_FIELD = "node_id"
SINK_NODE_ID_FIELD = "sink_node_id"
SOURCE_ENDPOINT_FIELD = "source_end_point"
DESTINATION_ENDPOINT_FIELD = "destination_end_point"
PAYLOAD_FIELD = "payload"
QOS_FIELD = "qos"
RERUN_INTERVAL_FIELD = "rerun_interval_s"
IS_CLOSE_FIELD = "is_close"
ALTITUDE_LEFTBOTTOM_FIELD = "altitude_leftbottom"
ALTITUDE_LEFTTOP_FIELD = "altitude_lefttop"
ALTITUDE_RIGHTBOTTOM_FIELD = "altitude_rightbottom"
ALTITUDE_RIGHTTOP_FIELD = "altitude_righttop"
DISTANCE_IN_M_FIELD = "distance_in_m"
LATITUDE_LEFTBOTTOM_FIELD = "latitude_leftbottom"
LATITUDE_LEFTTOP_FIELD = "latitude_lefttop"
LATITUDE_RIGHTBOTTOM_FIELD = "latitude_rightbottom"
LATITUDE_RIGHTTOP_FIELD = "latitude_righttop"
LONGITUDE_LEFTBOTTOM_FIELD = "longitude_leftbottom"
LONGITUDE_LEFTTOP_FIELD = "longitude_lefttop"
LONGITUDE_RIGHTBOTTOM_FIELD = "longitude_rightbottom"
LONGITUDE_RIGHTTOP_FIELD = "longitude_righttop"
X_DISTANCE_POINT1_FIELD = "x_distance_point1"
X_DISTANCE_POINT2_FIELD = "x_distance_point2"
X_NORMCOORD_LEFTBOTTOM_FIELD = "x_normcoord_leftbottom"
X_NORMCOORD_LEFTTOP_FIELD = "x_normcoord_lefttop"
X_NORMCOORD_RIGHTBOTTOM_FIELD = "x_normcoord_rightbottom"
X_NORMCOORD_RIGHTTOP_FIELD = "x_normcoord_righttop"
Y_DISTANCE_POINT1_FIELD = "y_distance_point1"
Y_DISTANCE_POINT2_FIELD = "y_distance_point2"
Y_NORMCOORD_LEFTBOTTOM_FIELD = "y_normcoord_leftbottom"
Y_NORMCOORD_LEFTTOP_FIELD = "y_normcoord_lefttop"
Y_NORMCOORD_RIGHTBOTTOM_FIELD = "y_normcoord_rightbottom"
Y_NORMCOORD_RIGHTTOP_FIELD = "y_normcoord_righttop"
ALPHA_FIELD = "a"
RED_FIELD = "r"
GREEN_FIELD = "g"
BLUE_FIELD = "b"
METADATA_UPDATE_MESSAGE_FIELD = "metadata_update_message"
ADDED_OR_CHANGED_USERS_FIELD = "added_or_changed_users"
USERNAME_PROTO_FIELD = "user_name"
DELETED_USERS_FIELD = "deleted_users"
ADDED_OR_CHANGED_BUILDINGS_FIELD = "added_or_changed_buildings"
ADDED_OR_CHANGED_FLOOR_PLANS_FIELD = "added_or_changed_floor_plans"
DELETED_FLOOR_PLANS_FIELD = "deleted_floor_plans"
BUILDING_ID_FIELD = "building_id"
ADDED_OR_CHANGED_NETWORKS_FIELD = "added_or_changed_networks"

NULL = "null"

TYPE_LOGIN = 1
TYPE_GET_USERS = 11
TYPE_CREATE_USER = 12
TYPE_UPDATE_USER = 13
TYPE_DELETE_USER = 14

TYPE_GET_BUILDINGS = 1001
TYPE_CREATE_BUILDING = 1002
TYPE_UPDATE_BUILDING = 1003
TYPE_DELETE_BUILDING = 1004

TYPE_GET_BUILDINGS_FLOOR_PLANS = 1011
TYPE_CREATE_FLOOR_PLAN = 1012
TYPE_UPDATE_FLOOR_PLAN = 1013
TYPE_DELETE_FLOOR_PLAN = 1014

TYPE_GET_FLOOR_PLAN_IMAGE_DATA = 1021
TYPE_SET_FLOOR_PLAN_IMAGE_DATA = 1022

TYPE_GET_MAP_AREAS = 1031
TYPE_CREATE_MAP_AREA = 1032
TYPE_UPDATE_MAP_AREA = 1033
TYPE_DELETE_MAP_AREA = 1034

TYPE_GET_NETWORKS = 1041
TYPE_CREATE_NETWORK = 1042
TYPE_UPDATE_NETWORK = 1043
TYPE_DELETE_NETWORK = 1044

TYPE_ADD_NODE_TO_FLOOR_PLAN = 1051
TYPE_REMOVE_NODE_FROM_FLOOR_PLAN = 1052

TYPE_SET_NODE_METADATA = 1061
TYPE_CHANGE_NODE_NETWORK_ID = 1062
TYPE_DELETE_NODE = 1063

TYPE_SET_NETWORK_DATA = 1071
TYPE_SEND_REMOTE_API_REQUEST = 1072
TYPE_SEND_DATA_MESSAGE = 1073
TYPE_GET_SCRATCHPAD_STATUS = 1074
TYPE_LOAD_SCRATCHPAD = 1075

TYPE_GET_COMPONENTS_INFORMATION = 1081

INVALID_ROLE = 0
ROLE_ADMIN = 1
ROLE_OPERATOR = 2

RESULT_OK = 1
GENERIC_ERROR = 2
INVALID_CREDENTIALS = 3
WRONG_PROTOCOL_VERSION = 4
USER_MISSING_RIGHTS = 5
INVALID_ID = 6
USER_ALREADY_EXISTS = 7
RECEIVED_MESSAGE_INVALID = 8
INVALID_SESSION_ID = 9

USERNAME_MINIMUM_LENGTH = 1
USERNAME_MAXIMUM_LENGTH = 63
PASSWORD_MINIMUM_LENGTH = 6
PASSWORD_MAXIMUM_LENGTH = 255
FULLNAME_MINIMUM_LENGTH = 1
FULLNAME_MAXIMUM_LENGTH = 255

SLEEP_WAITING_IN_S = 0.5
ORIGINATOR_TOKEN = str(uuid.uuid4())

NETWORK_ADDRESS_FIELD = "network_address"
NETWORK_NAME_FIELD = "network_name"
NODE_ADDRESS_FIELD = "node_address"
NODE_NAME_FIELD = "node_name"
FLOOR_PLAN_NAME_FIELD = "floor_plan_name"
BUILDING_NAME_FIELD = "building_name"
ONLINE_STATUS_FIELD = "online_status"
ONLINE_STATUS_STRING_FIELD = "online_status_string"
VOLTAGE_FIELD = "voltage"
POSITION_PIXEL_X_FIELD = "position_pixel_x"
POSITION_PIXEL_Y_FIELD = "position_pixel_y"
POSITION_METER_X_FIELD = "position_meter_x"
POSITION_METER_Y_FIELD = "position_meter_y"
POSITIONING_ROLE_FIELD = "positioning_role"
POSITIONING_ROLE_STRING_FIELD = "positioning_role_string"
MEASUREMENT_TIME_EPOCH_FIELD = "measurement_time_epoch"
MEASUREMENT_TIME_FIELD = "measurement_time"
POSITIONING_TIME_EPOCH_FIELD = "positioning_time_epoch"
POSITIONING_TIME_FIELD = "positioning_time"

LIST_JSON_FIELDS = [NETWORK_ADDRESS_FIELD, NETWORK_NAME_FIELD, NODE_ADDRESS_FIELD, NODE_NAME_FIELD,
                    ONLINE_STATUS_FIELD, ONLINE_STATUS_STRING_FIELD, VOLTAGE_FIELD, IS_APPROVED_FIELD, IS_VIRTUAL_FIELD,
                    LATITUDE_FIELD, LONGITUDE_FIELD, ALTITUDE_FIELD, POSITION_PIXEL_X_FIELD, POSITION_PIXEL_Y_FIELD,
                    POSITION_METER_X_FIELD, POSITION_METER_Y_FIELD, POSITIONING_ROLE_FIELD,
                    POSITIONING_ROLE_STRING_FIELD, MEASUREMENT_TIME_EPOCH_FIELD, MEASUREMENT_TIME_FIELD,
                    POSITIONING_TIME_EPOCH_FIELD, POSITIONING_TIME_FIELD, BUILDING_ID_FIELD, BUILDING_NAME_FIELD,
                    FLOOR_PLAN_ID_FIELD, FLOOR_PLAN_NAME_FIELD, AREAS_FIELD]

LIST_JSON_FIELDS_NOT_TO_COMPARE = [MEASUREMENT_TIME_EPOCH_FIELD, MEASUREMENT_TIME_FIELD, POSITIONING_TIME_EPOCH_FIELD,
                                   POSITIONING_TIME_FIELD]

LIST_FIELDS_TO_ROUND = [POSITION_PIXEL_X_FIELD, POSITION_PIXEL_Y_FIELD, POSITION_METER_X_FIELD, POSITION_METER_Y_FIELD]

ORIGINAL_DATA_FILE = os.path.join(".", "json_data", "original_data.json")
CURRENT_DATA_FILE = os.path.join(".", "json_data", "current_data.json")

WIREPAS_BUILDING_DATA = {"image_width": 3375, "image_height": 1901, "altitude_leftbottom": 0, "altitude_lefttop": 0,
                         "altitude_rightbottom": 0, "altitude_righttop": 0, "distance_in_m": 10,
                         "latitude_leftbottom": 61.44658, "latitude_lefttop": 61.446639,
                         "latitude_rightbottom": 61.446336, "latitude_righttop": 61.446405,
                         "longitude_leftbottom": 23.862209, "longitude_lefttop": 23.862534,
                         "longitude_rightbottom": 23.86245, "longitude_righttop": 23.86275,
                         "x_distance_point1": 0.969954595041732, "x_distance_point2": 0.968895412464479,
                         "x_normcoord_leftbottom": 0.419252468361556, "x_normcoord_lefttop": 0.404677874547788,
                         "x_normcoord_rightbottom": 0.931623691528882, "x_normcoord_righttop": 0.931033177949218,
                         "y_distance_point1": 0.735277696013156, "y_distance_point2": 0.425390617960317,
                         "y_normcoord_leftbottom": 0.759663480205769, "y_normcoord_lefttop": 0.119067770181991,
                         "y_normcoord_rightbottom": 0.757714205674469, "y_normcoord_righttop": 0.12117205176376}

NODES_TESTS_BUILDING_DATA = {"image_width": 3375, "image_height": 1901, "altitude_leftbottom": 0, "altitude_lefttop": 0,
                         "altitude_rightbottom": 0, "altitude_righttop": 0, "distance_in_m": 10,
                         "latitude_leftbottom": 61.44658, "latitude_lefttop": 61.446639,
                         "latitude_rightbottom": 61.446336, "latitude_righttop": 61.446405,
                         "longitude_leftbottom": 23.862209, "longitude_lefttop": 23.862534,
                         "longitude_rightbottom": 23.86245, "longitude_righttop": 23.86275,
                         "x_distance_point1": 0.969954595041732, "x_distance_point2": 0.968895412464479,
                         "x_normcoord_leftbottom": 0.419252468361556, "x_normcoord_lefttop": 0.404677874547788,
                         "x_normcoord_rightbottom": 0.931623691528882, "x_normcoord_righttop": 0.931033177949218,
                         "y_distance_point1": 0.735277696013156, "y_distance_point2": 0.425390617960317,
                         "y_normcoord_leftbottom": 0.759663480205769, "y_normcoord_lefttop": 0.119067770181991,
                         "y_normcoord_rightbottom": 0.757714205674469, "y_normcoord_righttop": 0.12117205176376}

NEW_USER_NAME = "newUser"
NEW_USER_PASSWORD = "newPassword"
NEW_USER_FULLNAME = "new user full name"
NEW_ADMIN_NAME = "newAdmin"
NEW_ADMIN_PASSWORD = "newAdminPassword"
NEW_ADMIN_FULLNAME = "new admin full name"

NEW_USER_NAME_FOR_PASSWORD_PERCENT = "newUserPercent"
NEW_USER_NAME_FOR_PASSWORD_DOUBLE_QUOTE = "newUserDoubleQuote"
NEW_USER_NAME_FOR_PASSWORD_BACKSLASH = "newUserBackslash"
NEW_USER_NAME_FOR_PASSWORD_SPECIAL = "newUserSpecial"
PASSWORD_PERCENT = "%%password%"
PASSWORD_DOUBLE_QUOTE = "\"password\"\""
PASSWORD_BACKSLASH = "\\password\\\\"
PASSWORD_SPECIAL = "&@!#*$'()+-,./:;<>{}=?[]$_^~|"
UPDATED_PASSWORD_PERCENT = "updated%%password%"
UPDATED_PASSWORD_DOUBLE_QUOTE = "updated\"password\"\""
UPDATED_PASSWORD_BACKSLASH = "updated\\password\\\\"
UPDATED_PASSWORD_SPECIAL = "updated&@!#*$'()+-,./:;<>{}=?[]$_^~|"

UNUSED_USERNAME = "unused username"
UNUSED_USERNAME2 = "unused username 2"
NON_EXISTING_USER_NAME = "non existing username"
EMPTY_USERNAME = ""
TOO_LONG_USERNAME = "AAABBBCCCDDDEEEFFFGGGHHHIIIJJJKKKLLLMMMNNNOOOPPPQQQRRRSSSTTTUUUX"
TOO_SHORT_PASSWORD = "short"
TOO_LONG_PASSWORD = "AAAAAAAAAABBBBBBBBBBCCCCCCCCCCDDDDDDDDDDEEEEEEEEEE" \
                    "FFFFFFFFFFGGGGGGGGGGHHHHHHHHHHIIIIIIIIIIJJJJJJJJJJ" \
                    "KKKKKKKKKKLLLLLLLLLLMMMMMMMMMMNNNNNNNNNNOOOOOOOOOO" \
                    "PPPPPPPPPPQQQQQQQQQQRRRRRRRRRRSSSSSSSSSSTTTTTTTTTT" \
                    "UUUUUUUUUUVVVVVVVVVVWWWWWWWWWWXXXXXXXXXXYYYYYYYYYY" \
                    "ZZZZZ0"

TOO_SHORT_FULL_NAME = ""
TOO_LONG_FULL_NAME = "AAAAAAAAAABBBBBBBBBBCCCCCCCCCCDDDDDDDDDDEEEEEEEEEE" \
                    "FFFFFFFFFFGGGGGGGGGGHHHHHHHHHHIIIIIIIIIIJJJJJJJJJJ" \
                    "KKKKKKKKKKLLLLLLLLLLMMMMMMMMMMNNNNNNNNNNOOOOOOOOOO" \
                    "PPPPPPPPPPQQQQQQQQQQRRRRRRRRRRSSSSSSSSSSTTTTTTTTTT" \
                    "UUUUUUUUUUVVVVVVVVVVWWWWWWWWWWXXXXXXXXXXYYYYYYYYYY" \
                    " ZZZZZ"

UPDATED_OPERATOR_PASSWORD = "updatedOperatorPassword"
UPDATED_ADMIN_PASSWORD = "updatedAdminPassword"
UPDATED_FULL_NAME = "updated full name"
UPDATED_FULL_NAME_ALL = "new updated full name"
UPDATED_PASSWORD_ALL = "newUpdatedPassword"

USER_TO_BE_DELETED_NAME = "UserToBeDeleted"
USER_TO_BE_DELETED_FULLNAME = "User To Be Deleted"
USER_TO_BE_DELETED_PASSWORD = "password2delete"

ADMIN_TO_BE_DELETED_NAME = "AdminToBeDeleted"
ADMIN_TO_BE_DELETED_FULLNAME = "Admin To Be Deleted"
ADMIN_TO_BE_DELETED_PASSWORD = "password2delete2"

NEW_BUILDING_NAME = "New building name"
UPDATED_BUILDING_NAME = "Updated building name"
UNUSED_BUILDING_NAME = "Unused building name"
UNUSED_BUILDING_NAME2 = "Unused building name 2"
EMPTY_NAME = ""
TOO_LONG_BUILDING_NAME = "AAAAAAAAAABBBBBBBBBBCCCCCCCCCCDDDDDDDDDDEEEEEEEEEE" \
                    "FFFFFFFFFFGGGGGGGGGGHHHHHHHHHHIIIIIIIIIIJJJJJJJJJJ" \
                    "KKKKKKKKKKLLLLLLLLLLMMMMMMMMMMNNNNNNNNNNOOOOOOOOOO" \
                    "PPPPPPPPPPQQQQQQQQQQRRRRRRRRRRSSSSSSSSSSTTTTTTTTTT" \
                    "UUUUUUUUUUVVVVVVVVVVWWWWWWWWWWXXXXXXXXXXYYYYYYYYYY" \
                    "ZZZZZ0"

BUILDING_DEDICATED_FOR_FLOOR_PLANS = "building for floor plans"
BUILDING_DEDICATED_FOR_FLOOR_PLANS2 = "building for floor plans 2"
BUILDING_DEDICATED_FOR_NODES = "building for nodes"
FLOOR_PLAN_NAME = "some floor plan"
FLOOR_PLAN_NAME2 = "some floor plan 2"
UNUSED_FLOOR_PLAN_NAME = "unused floor plan name"
UNUSED_FLOOR_PLAN_NAME2 = "unused floor plan name 2"
FLOOR_PLAN_FOR_NODES = "floor plan for nodes"
LEVEL_2 = 2
FLOAT_LEVEL = 3.3
FLOOR_PLAN_IMAGE_DATA_PATH = os.path.join(".", "tests", "H3_wirepas_floorplan.png")
FLOOR_PLAN_THUMBNAIL_DATA_PATH = os.path.join(".", "tests", "H3_wirepas_floorplanMini.png")
INTERNAL_IMAGE_NAME = "floor_plan_image"
INTERNAL_THUMBNAIL_IMAGE_NAME = "floor_plan_thumbnail_image"

NEW_NETWORK_NAME = "New Network"
UPDATED_NETWORK_NAME = "Updated New Network"
UNUSED_NETWORK_NAME = "Unused Network Name"
UNUSED_NETWORK_NAME2 = "Unused Network Name 2"
EMPTY_NETWORK_NAME = ""

NEW_NETWORK_ID = "1000"
NEW_NETWORK_ID_2 = "1001"
UNUSED_NETWORK_ID = "1002"
UNUSED_NETWORK_ID2 = "1003"
EMPTY_NETWORK_ID = ""
NETWORK_ID_0 = "0"
NETWORK_ID_16777216 = "16777216"

SINK_ID = "1"
NODE_ID = "2"
SUBNODE_ID = "3"
NODE_NETWORK_ID = "123"
INVALID_NODE_ID = "0"
NODE_IS_SINK = False

VIRTUAL_SINK_ID = "1"
VIRTUAL_NODE_ID = "2"
VIRTUAL_SUBNODE_ID = "3"
VIRTUAL_NODE_NETWORK_ID = "1234"
VIRTUAL_NODE_NAME = "virtual node name"
VIRTUAL_NODE_DESCRIPTION = "virtual node description"
VIRTUAL_NODE_POSITION = {"latitude": 0, "longitude": 0, "altitude": 0}
VIRTUAL_NODE_IS_VIRTUAL = True
VIRTUAL_NODE_IS_APPROVED = True

INVALID_FLOOR_PLAN_ID = "0"

NODE_METADATA_ID = "4"
NODE_METADATA_NETWORK_ID = "123"
NODE_METADATA_NAME = "node metadata test name"
NODE_METADATA_DESCRIPTION = "node metadata test node description"
NODE_METADATA_IS_APPROVED = True
NODE_METADATA_IS_VIRTUAL = False
NODE_METADATA_POSITION = {"latitude": 0, "longitude": 0, "altitude": 0}
NODE_METADATA_IS_SINK = False

VIRTUAL_NODE_METADATA_ID = "5"
VIRTUAL_NODE_METADATA_NETWORK_ID = "123"
VIRTUAL_NODE_METADATA_NAME = "virtual node metadata name"
VIRTUAL_NODE_METADATA_DESCRIPTION = "virtual node metadata test node description"
VIRTUAL_NODE_METADATA_IS_APPROVED = True
VIRTUAL_NODE_METADATA_IS_VIRTUAL = True
VIRTUAL_NODE_METADATA_POSITION = {"latitude": 0, "longitude": 0, "altitude": 0}
VIRTUAL_NODE_METADATA_IS_SINK = False

NODE_ID_WITH_INVALID_NAME = "6"
INVALID_NODE_NAME = '"\\ invalid node name'

NODE_NAME_WITH_INVALID_DESCRIPTION = "node with invalid description"
NODE_ID_WITH_INVALID_DESCRIPTION = "7"
INVALID_NODE_DESCRIPTION = '"\\ invalid node description'

NON_EXISTANT_NODE_ID = "999"
NON_EXISTANT_NODE_IS_SINK = False

APPLICATION_DATA = "112233445566778899AABBCCDDEEFF"
DIAGNOSTICS_INTERVAL = "30"
IS_OVERRIDE_ON = False
INVALID_APP_DATA = "0"