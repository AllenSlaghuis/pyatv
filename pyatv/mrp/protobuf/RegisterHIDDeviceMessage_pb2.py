# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pyatv/mrp/protobuf/RegisterHIDDeviceMessage.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pyatv.mrp.protobuf import ProtocolMessage_pb2 as pyatv_dot_mrp_dot_protobuf_dot_ProtocolMessage__pb2
from pyatv.mrp.protobuf import VirtualTouchDeviceDescriptorMessage_pb2 as pyatv_dot_mrp_dot_protobuf_dot_VirtualTouchDeviceDescriptorMessage__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pyatv/mrp/protobuf/RegisterHIDDeviceMessage.proto',
  package='',
  syntax='proto2',
  serialized_pb=_b('\n1pyatv/mrp/protobuf/RegisterHIDDeviceMessage.proto\x1a(pyatv/mrp/protobuf/ProtocolMessage.proto\x1a<pyatv/mrp/protobuf/VirtualTouchDeviceDescriptorMessage.proto\"S\n\x18RegisterHIDDeviceMessage\x12\x37\n\x10\x64\x65viceDescriptor\x18\x01 \x01(\x0b\x32\x1d.VirtualTouchDeviceDescriptor:M\n\x18registerHIDDeviceMessage\x12\x10.ProtocolMessage\x18\x0b \x01(\x0b\x32\x19.RegisterHIDDeviceMessage')
  ,
  dependencies=[pyatv_dot_mrp_dot_protobuf_dot_ProtocolMessage__pb2.DESCRIPTOR,pyatv_dot_mrp_dot_protobuf_dot_VirtualTouchDeviceDescriptorMessage__pb2.DESCRIPTOR,])


REGISTERHIDDEVICEMESSAGE_FIELD_NUMBER = 11
registerHIDDeviceMessage = _descriptor.FieldDescriptor(
  name='registerHIDDeviceMessage', full_name='registerHIDDeviceMessage', index=0,
  number=11, type=11, cpp_type=10, label=1,
  has_default_value=False, default_value=None,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  options=None, file=DESCRIPTOR)


_REGISTERHIDDEVICEMESSAGE = _descriptor.Descriptor(
  name='RegisterHIDDeviceMessage',
  full_name='RegisterHIDDeviceMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='deviceDescriptor', full_name='RegisterHIDDeviceMessage.deviceDescriptor', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=157,
  serialized_end=240,
)

_REGISTERHIDDEVICEMESSAGE.fields_by_name['deviceDescriptor'].message_type = pyatv_dot_mrp_dot_protobuf_dot_VirtualTouchDeviceDescriptorMessage__pb2._VIRTUALTOUCHDEVICEDESCRIPTOR
DESCRIPTOR.message_types_by_name['RegisterHIDDeviceMessage'] = _REGISTERHIDDEVICEMESSAGE
DESCRIPTOR.extensions_by_name['registerHIDDeviceMessage'] = registerHIDDeviceMessage
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RegisterHIDDeviceMessage = _reflection.GeneratedProtocolMessageType('RegisterHIDDeviceMessage', (_message.Message,), dict(
  DESCRIPTOR = _REGISTERHIDDEVICEMESSAGE,
  __module__ = 'pyatv.mrp.protobuf.RegisterHIDDeviceMessage_pb2'
  # @@protoc_insertion_point(class_scope:RegisterHIDDeviceMessage)
  ))
_sym_db.RegisterMessage(RegisterHIDDeviceMessage)

registerHIDDeviceMessage.message_type = _REGISTERHIDDEVICEMESSAGE
pyatv_dot_mrp_dot_protobuf_dot_ProtocolMessage__pb2.ProtocolMessage.RegisterExtension(registerHIDDeviceMessage)

# @@protoc_insertion_point(module_scope)
