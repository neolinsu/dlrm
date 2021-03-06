# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: config.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='config.proto',
  package='hybridtraining',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\x0c\x63onfig.proto\x12\x0ehybridtraining\"!\n\rConfigRequest\x12\x10\n\x08hostname\x18\x01 \x01(\t\"U\n\x0b\x43onfigReply\x12\x11\n\tsparseOpt\x18\x01 \x01(\t\x12\x10\n\x08\x64\x65nseOpt\x18\x02 \x01(\t\x12\x10\n\x08sparseLR\x18\x03 \x01(\x02\x12\x0f\n\x07\x64\x65nseLR\x18\x04 \x01(\x02\x32S\n\x06\x43onfig\x12I\n\tGetConfig\x12\x1d.hybridtraining.ConfigRequest\x1a\x1b.hybridtraining.ConfigReply\"\x00\x62\x06proto3'
)




_CONFIGREQUEST = _descriptor.Descriptor(
  name='ConfigRequest',
  full_name='hybridtraining.ConfigRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='hostname', full_name='hybridtraining.ConfigRequest.hostname', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=32,
  serialized_end=65,
)


_CONFIGREPLY = _descriptor.Descriptor(
  name='ConfigReply',
  full_name='hybridtraining.ConfigReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='sparseOpt', full_name='hybridtraining.ConfigReply.sparseOpt', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='denseOpt', full_name='hybridtraining.ConfigReply.denseOpt', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sparseLR', full_name='hybridtraining.ConfigReply.sparseLR', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='denseLR', full_name='hybridtraining.ConfigReply.denseLR', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=67,
  serialized_end=152,
)

DESCRIPTOR.message_types_by_name['ConfigRequest'] = _CONFIGREQUEST
DESCRIPTOR.message_types_by_name['ConfigReply'] = _CONFIGREPLY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ConfigRequest = _reflection.GeneratedProtocolMessageType('ConfigRequest', (_message.Message,), {
  'DESCRIPTOR' : _CONFIGREQUEST,
  '__module__' : 'config_pb2'
  # @@protoc_insertion_point(class_scope:hybridtraining.ConfigRequest)
  })
_sym_db.RegisterMessage(ConfigRequest)

ConfigReply = _reflection.GeneratedProtocolMessageType('ConfigReply', (_message.Message,), {
  'DESCRIPTOR' : _CONFIGREPLY,
  '__module__' : 'config_pb2'
  # @@protoc_insertion_point(class_scope:hybridtraining.ConfigReply)
  })
_sym_db.RegisterMessage(ConfigReply)



_CONFIG = _descriptor.ServiceDescriptor(
  name='Config',
  full_name='hybridtraining.Config',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=154,
  serialized_end=237,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetConfig',
    full_name='hybridtraining.Config.GetConfig',
    index=0,
    containing_service=None,
    input_type=_CONFIGREQUEST,
    output_type=_CONFIGREPLY,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_CONFIG)

DESCRIPTOR.services_by_name['Config'] = _CONFIG

# @@protoc_insertion_point(module_scope)
