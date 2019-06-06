# unicode string for Py2 / Py3
from builtins import str as ustr

import json

from ..core.baseformat import BaseFormat
from .. import core


class JSONFormat(BaseFormat):

    _name = "JSON"
    _extension = ".json"
    _priority = 100

    def _write_file(self, filepath, data, **options):
        json_str = ustr(json.dumps(data, ensure_ascii=False))
        filepath.write_text(json_str)

    def _read_file(self, filepath, **options):
        json_str = filepath.read_text()
        return json.loads(json_str)


# register class
core.formats.register_class(JSONFormat)
