from collections import OrderedDict
import csv

from ..core.person import Person
from ..core.baseformat import BaseFormat
from .. import core


class CSVFormat(BaseFormat):

    _name = "CSV"
    _extension = ".csv"

    def _write_file(self, filepath, data, **options):
        with filepath.open("wb+") as csvfile:
            writer = csv.DictWriter(csvfile, dialect=csv.excel, fieldnames=Person.fields())
            writer.writeheader()
            writer.writerows(data)

    def _read_file(self, filepath, **options): # TODO: Does not maintain order yet!
        with filepath.open("rb") as csvfile:
            reader = csv.DictReader(csvfile)
            return list(reader)


# register class
core.formats.register_class(CSVFormat)
