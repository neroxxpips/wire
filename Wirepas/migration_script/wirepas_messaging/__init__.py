"""
    WNT
    ===
    Wirepas Network Tool metadata - and realtime situation message definitions

    Metadata message protocol version compatibility
    Version 2: WNT backend 1.7.x
    Version 3: WNT backend 2.0.x

"""

from . import gateway
from . import nanopb

try:
    from . import wnt
except ImportError as err:
    wnt = "Not available - please compile protos prior to manual install."
    print("Could not import WPE handles ({})".format(err))

from google.protobuf.internal import api_implementation


# pylint: disable=locally-disabled, protected-access, wrong-import-order
try:
    if api_implementation._default_implementation_type == "python":
        print("api_implementation default is python")
except AttributeError:
    print("Could not evaluate protobuf implementation type")


__all__ = [
    "gateway",
    "nanopb",
    "wnt",
]
