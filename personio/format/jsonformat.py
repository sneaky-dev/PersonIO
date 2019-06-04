from ..core.baseformat import BaseFormat
from .. import core


class JSONFormat(BaseFormat):

    _label = "JSON"
    _extension = ".json"

    def _write_file(self, filepath, data, **kwargs):
        pass

    def _read_file(self, filepath, **kwargs):
        pass


# register class
core.formats.register_class(JSONFormat)
