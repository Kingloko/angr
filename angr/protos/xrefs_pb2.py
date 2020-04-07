# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protos/xrefs.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import primitives_pb2 as protos_dot_primitives__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='protos/xrefs.proto',
  package='angr.protos',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x12protos/xrefs.proto\x12\x0b\x61ngr.protos\x1a\x17protos/primitives.proto\"2\n\x05XRefs\x12)\n\x05xrefs\x18\x01 \x03(\x0b\x32\x1a.angr.protos.CodeReferenceb\x06proto3')
  ,
  dependencies=[protos_dot_primitives__pb2.DESCRIPTOR,])




_XREFS = _descriptor.Descriptor(
  name='XRefs',
  full_name='angr.protos.XRefs',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='xrefs', full_name='angr.protos.XRefs.xrefs', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=60,
  serialized_end=110,
)

_XREFS.fields_by_name['xrefs'].message_type = protos_dot_primitives__pb2._CODEREFERENCE
DESCRIPTOR.message_types_by_name['XRefs'] = _XREFS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

XRefs = _reflection.GeneratedProtocolMessageType('XRefs', (_message.Message,), dict(
  DESCRIPTOR = _XREFS,
  __module__ = 'protos.xrefs_pb2'
  # @@protoc_insertion_point(class_scope:angr.protos.XRefs)
  ))
_sym_db.RegisterMessage(XRefs)


# @@protoc_insertion_point(module_scope)
