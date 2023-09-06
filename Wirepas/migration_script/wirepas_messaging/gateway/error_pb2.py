# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: wirepas_messaging/gateway/error.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='wirepas_messaging/gateway/error.proto',
  package='com.wirepas.proto.gateway',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n%wirepas_messaging/gateway/error.proto\x12\x19\x63om.wirepas.proto.gateway*\xf9\x04\n\tErrorCode\x12\x06\n\x02OK\x10\x00\x12\x12\n\x0eINTERNAL_ERROR\x10\x01\x12\x13\n\x0fINVALID_SINK_ID\x10\x02\x12\x10\n\x0cINVALID_ROLE\x10\x03\x12\x1b\n\x17INVALID_NETWORK_ADDRESS\x10\x04\x12\x1b\n\x17INVALID_NETWORK_CHANNEL\x10\x05\x12\x17\n\x13INVALID_CHANNEL_MAP\x10\x06\x12\x18\n\x14INVALID_NETWORK_KEYS\x10\x07\x12\x14\n\x10INVALID_AC_RANGE\x10\x08\x12\x16\n\x12INVALID_SINK_STATE\x10\t\x12\x18\n\x14INVALID_DEST_ADDRESS\x10\n\x12\x19\n\x15INVALID_DEST_ENDPOINT\x10\x0b\x12\x18\n\x14INVALID_SRC_ENDPOINT\x10\x0c\x12\x0f\n\x0bINVALID_QOS\x10\r\x12\x18\n\x14INVALID_DATA_PAYLOAD\x10\x0e\x12\x16\n\x12INVALID_SCRATCHPAD\x10\x0f\x12\x1b\n\x17INVALID_SCRATCHPAD_SIZE\x10\x10\x12\x1b\n\x17INVLAID_SEQUENCE_NUMBER\x10\x11\x12\x18\n\x14INVALID_REBOOT_DELAY\x10\x12\x12\x19\n\x15INVALID_DIAG_INTERVAL\x10\x13\x12\x16\n\x12INVALID_APP_CONFIG\x10\x14\x12\x11\n\rINVALID_PARAM\x10\x15\x12\x19\n\x15NO_SCRATCHPAD_PRESENT\x10\x16\x12\x11\n\rACCESS_DENIED\x10\x17\x12\x19\n\x15REQUEST_NEEDS_SINK_ID\x10\x18\x12\x19\n\x15INVALID_MAX_HOP_COUNT\x10\x19')
)

_ERRORCODE = _descriptor.EnumDescriptor(
  name='ErrorCode',
  full_name='com.wirepas.proto.gateway.ErrorCode',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='OK', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INTERNAL_ERROR', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_SINK_ID', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_ROLE', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_NETWORK_ADDRESS', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_NETWORK_CHANNEL', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_CHANNEL_MAP', index=6, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_NETWORK_KEYS', index=7, number=7,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_AC_RANGE', index=8, number=8,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_SINK_STATE', index=9, number=9,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_DEST_ADDRESS', index=10, number=10,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_DEST_ENDPOINT', index=11, number=11,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_SRC_ENDPOINT', index=12, number=12,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_QOS', index=13, number=13,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_DATA_PAYLOAD', index=14, number=14,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_SCRATCHPAD', index=15, number=15,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_SCRATCHPAD_SIZE', index=16, number=16,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVLAID_SEQUENCE_NUMBER', index=17, number=17,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_REBOOT_DELAY', index=18, number=18,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_DIAG_INTERVAL', index=19, number=19,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_APP_CONFIG', index=20, number=20,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_PARAM', index=21, number=21,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NO_SCRATCHPAD_PRESENT', index=22, number=22,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ACCESS_DENIED', index=23, number=23,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REQUEST_NEEDS_SINK_ID', index=24, number=24,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_MAX_HOP_COUNT', index=25, number=25,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=69,
  serialized_end=702,
)
_sym_db.RegisterEnumDescriptor(_ERRORCODE)

ErrorCode = enum_type_wrapper.EnumTypeWrapper(_ERRORCODE)
OK = 0
INTERNAL_ERROR = 1
INVALID_SINK_ID = 2
INVALID_ROLE = 3
INVALID_NETWORK_ADDRESS = 4
INVALID_NETWORK_CHANNEL = 5
INVALID_CHANNEL_MAP = 6
INVALID_NETWORK_KEYS = 7
INVALID_AC_RANGE = 8
INVALID_SINK_STATE = 9
INVALID_DEST_ADDRESS = 10
INVALID_DEST_ENDPOINT = 11
INVALID_SRC_ENDPOINT = 12
INVALID_QOS = 13
INVALID_DATA_PAYLOAD = 14
INVALID_SCRATCHPAD = 15
INVALID_SCRATCHPAD_SIZE = 16
INVLAID_SEQUENCE_NUMBER = 17
INVALID_REBOOT_DELAY = 18
INVALID_DIAG_INTERVAL = 19
INVALID_APP_CONFIG = 20
INVALID_PARAM = 21
NO_SCRATCHPAD_PRESENT = 22
ACCESS_DENIED = 23
REQUEST_NEEDS_SINK_ID = 24
INVALID_MAX_HOP_COUNT = 25


DESCRIPTOR.enum_types_by_name['ErrorCode'] = _ERRORCODE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)


# @@protoc_insertion_point(module_scope)
