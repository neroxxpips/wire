import json
from json import JSONEncoder

from wirepas_messaging import wnt as wnt_proto


class MigrationData:
    def __init__(self, wnt_message: wnt_proto.Message):
        self.network_id = int
        self.id = int
        self.diagnostics_role = wnt_proto.commons_pb2.BaseRole
        self.node_metadata_latitude = float
        self.node_metadata_longitude = float
        self.node_metadata_altitude = float
        self.node_metadata_is_approved = False
        self.is_anchor = False

        if wnt_message.HasField("network_id"):
            self.network_id = wnt_message.network_id
        if wnt_message.HasField("source_address"):
            self.id = wnt_message.source_address
        if wnt_message.HasField("diagnostics"):
            if wnt_message.diagnostics.HasField("role"):
                self.diagnostics_role = wnt_message.diagnostics.role
        if wnt_message.HasField("node_metadata"):
            if wnt_message.node_metadata.HasField("latitude"):
                self.node_metadata_latitude = wnt_message.node_metadata.latitude
            if wnt_message.node_metadata.HasField("longitude"):
                self.node_metadata_longitude = wnt_message.node_metadata.longitude
            if wnt_message.node_metadata.HasField("altitude"):
                self.node_metadata_altitude = wnt_message.node_metadata.altitude
            if wnt_message.node_metadata.HasField("is_approved"):
                self.node_metadata_is_approved = wnt_message.node_metadata.is_approved
        if self.diagnostics_role == wnt_proto.commons_pb2.BaseRole.HEADNODE \
                and isinstance(self.node_metadata_latitude, type(float())) \
                and isinstance(self.node_metadata_longitude, type(float())) \
                and isinstance(self.node_metadata_altitude, type(float())) \
                and self.node_metadata_is_approved:
            self.is_anchor = True


class MigrationDataJsonEncoder(JSONEncoder):
    def default(self, object_to_encode):
        if isinstance(object_to_encode, MigrationData):
            return object_to_encode.__dict__
        else:
            return json.JSONEncoder.default(self, object_to_encode)