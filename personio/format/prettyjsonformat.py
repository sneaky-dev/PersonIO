# unicode string for Py2 / Py3
from builtins import str as ustr

import json

from ..core.baseformat import BaseFormat
from .. import core


class PrettyJSONFormat(BaseFormat):
    """Alternative JSON Reader / Writer implementation.
    Writes the data formatted more human-friendly then the default JSON format class.
    """

    _name = "PrettyJSON"
    _extension = ".json"
    _priority = 0

    def _write_file(self, filepath, data, **options):
        options = {
            "sort_keys": True,
            "indent": 4,
            "separators": (',', ': '),
            "ensure_ascii": False
        }
        json_str = ustr(json.dumps(data, **options))
        filepath.write_text(json_str)

    def _read_file(self, filepath, **options):
        json_str = filepath.read_text()
        return json.loads(json_str)


# register class
core.formats.register_class(PrettyJSONFormat)
