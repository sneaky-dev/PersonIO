from collections import OrderedDict
import csv

import six

from ..core.person import Person
from ..core.baseformat import BaseFormat
from .. import core


class CSVFormat(BaseFormat):
    """CSV file format.
    Reads / Writes CSV data.

    Note: CSV input data needs to have a valid header row.
    """

    _name = "CSV"
    _extension = ".csv"

    def _write_file(self, filepath, data, **options):
        with filepath.open("wb+" if six.PY2 else "w+") as csvfile:
            writer = csv.DictWriter(csvfile, dialect=csv.excel, fieldnames=Person.fields())
            writer.writeheader()
            writer.writerows(data)

    def _read_file(self, filepath, **options):
        with filepath.open("rb" if six.PY2 else "r") as csvfile:
            reader = csv.DictReader(csvfile)
            return list(reader)


# register class
core.formats.register_class(CSVFormat)
