# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: celestial.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0f\x63\x65lestial.proto\x12 openfogstack.celestial.celestial\"&\n\tMachineID\x12\r\n\x05group\x18\x01 \x01(\r\x12\n\n\x02id\x18\x02 \x01(\r\"\x07\n\x05\x45mpty\"\x1f\n\x0fRegisterRequest\x12\x0c\n\x04host\x18\x01 \x01(\r\"t\n\x10RegisterResponse\x12\x16\n\x0e\x61vailable_cpus\x18\x01 \x01(\r\x12\x15\n\ravailable_ram\x18\x02 \x01(\x04\x12\x17\n\x0fpeer_public_key\x18\x03 \x01(\t\x12\x18\n\x10peer_listen_addr\x18\x04 \x01(\t\"\xa7\x04\n\x0bInitRequest\x12\x41\n\x05hosts\x18\x01 \x03(\x0b\x32\x32.openfogstack.celestial.celestial.InitRequest.Host\x12G\n\x08machines\x18\x02 \x03(\x0b\x32\x35.openfogstack.celestial.celestial.InitRequest.Machine\x1a\x45\n\x04Host\x12\n\n\x02id\x18\x01 \x01(\r\x12\x17\n\x0fpeer_public_key\x18\x02 \x01(\t\x12\x18\n\x10peer_listen_addr\x18\x03 \x01(\t\x1a\xc4\x02\n\x07Machine\x12\x37\n\x02id\x18\x01 \x01(\x0b\x32+.openfogstack.celestial.celestial.MachineID\x12\x11\n\x04name\x18\x02 \x01(\tH\x00\x88\x01\x01\x12\x0c\n\x04host\x18\x03 \x01(\r\x12S\n\x06\x63onfig\x18\x04 \x01(\x0b\x32\x43.openfogstack.celestial.celestial.InitRequest.Machine.MachineConfig\x1a\x80\x01\n\rMachineConfig\x12\x12\n\nvcpu_count\x18\x01 \x01(\r\x12\x0b\n\x03ram\x18\x02 \x01(\x04\x12\x11\n\tdisk_size\x18\x03 \x01(\x04\x12\x12\n\nroot_image\x18\x04 \x01(\t\x12\x0e\n\x06kernel\x18\x05 \x01(\t\x12\x17\n\x0f\x62oot_parameters\x18\x06 \x03(\tB\x07\n\x05_name\"\xff\x04\n\x12StateUpdateRequest\x12W\n\rmachine_diffs\x18\x01 \x03(\x0b\x32@.openfogstack.celestial.celestial.StateUpdateRequest.MachineDiff\x12W\n\rnetwork_diffs\x18\x02 \x03(\x0b\x32@.openfogstack.celestial.celestial.StateUpdateRequest.NetworkDiff\x1a\x81\x01\n\x0bMachineDiff\x12\x39\n\x06\x61\x63tive\x18\x01 \x01(\x0e\x32).openfogstack.celestial.celestial.VMState\x12\x37\n\x02id\x18\x02 \x01(\x0b\x32+.openfogstack.celestial.celestial.MachineID\x1a\xb2\x02\n\x0bNetworkDiff\x12\x0f\n\x07\x62locked\x18\x01 \x01(\x08\x12;\n\x06source\x18\x02 \x01(\x0b\x32+.openfogstack.celestial.celestial.MachineID\x12;\n\x06target\x18\x03 \x01(\x0b\x32+.openfogstack.celestial.celestial.MachineID\x12\x0f\n\x07latency\x18\x04 \x01(\r\x12\x11\n\tbandwidth\x18\x05 \x01(\x04\x12\x39\n\x04next\x18\x06 \x01(\x0b\x32+.openfogstack.celestial.celestial.MachineID\x12\x39\n\x04prev\x18\x07 \x01(\x0b\x32+.openfogstack.celestial.celestial.MachineID*4\n\x07VMState\x12\x14\n\x10VM_STATE_STOPPED\x10\x00\x12\x13\n\x0fVM_STATE_ACTIVE\x10\x01\x32\xa3\x03\n\tCelestial\x12q\n\x08Register\x12\x31.openfogstack.celestial.celestial.RegisterRequest\x1a\x32.openfogstack.celestial.celestial.RegisterResponse\x12^\n\x04Init\x12-.openfogstack.celestial.celestial.InitRequest\x1a\'.openfogstack.celestial.celestial.Empty\x12i\n\x06Update\x12\x34.openfogstack.celestial.celestial.StateUpdateRequest\x1a\'.openfogstack.celestial.celestial.Empty(\x01\x12X\n\x04Stop\x12\'.openfogstack.celestial.celestial.Empty\x1a\'.openfogstack.celestial.celestial.EmptyB\x0eZ\x0c./;celestialb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'celestial_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z\014./;celestial'
  _globals['_VMSTATE']._serialized_start=1449
  _globals['_VMSTATE']._serialized_end=1501
  _globals['_MACHINEID']._serialized_start=53
  _globals['_MACHINEID']._serialized_end=91
  _globals['_EMPTY']._serialized_start=93
  _globals['_EMPTY']._serialized_end=100
  _globals['_REGISTERREQUEST']._serialized_start=102
  _globals['_REGISTERREQUEST']._serialized_end=133
  _globals['_REGISTERRESPONSE']._serialized_start=135
  _globals['_REGISTERRESPONSE']._serialized_end=251
  _globals['_INITREQUEST']._serialized_start=254
  _globals['_INITREQUEST']._serialized_end=805
  _globals['_INITREQUEST_HOST']._serialized_start=409
  _globals['_INITREQUEST_HOST']._serialized_end=478
  _globals['_INITREQUEST_MACHINE']._serialized_start=481
  _globals['_INITREQUEST_MACHINE']._serialized_end=805
  _globals['_INITREQUEST_MACHINE_MACHINECONFIG']._serialized_start=668
  _globals['_INITREQUEST_MACHINE_MACHINECONFIG']._serialized_end=796
  _globals['_STATEUPDATEREQUEST']._serialized_start=808
  _globals['_STATEUPDATEREQUEST']._serialized_end=1447
  _globals['_STATEUPDATEREQUEST_MACHINEDIFF']._serialized_start=1009
  _globals['_STATEUPDATEREQUEST_MACHINEDIFF']._serialized_end=1138
  _globals['_STATEUPDATEREQUEST_NETWORKDIFF']._serialized_start=1141
  _globals['_STATEUPDATEREQUEST_NETWORKDIFF']._serialized_end=1447
  _globals['_CELESTIAL']._serialized_start=1504
  _globals['_CELESTIAL']._serialized_end=1923
# @@protoc_insertion_point(module_scope)
