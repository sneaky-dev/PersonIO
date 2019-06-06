from __future__ import print_function

from ..core.person import Person
from ..core.baseprinter import BasePrinter
from .. import core


class StdoutPrinter(BasePrinter):

    _name = "Stdout"

    def _print_data(self, data, **options):
        header_titles = Person.fields()
        columns = len(header_titles)

        # print header
        header_str = ("{:>20}" * columns).format(*header_titles)
        print("{}\n{}".format(header_str, "=" * len(header_str)))

        # print items
        print_items = [item.values() for item in data]
        row_format = "{:>20}" * columns
        for item in print_items:
            print(row_format.format(*item))


# register class
core.printers.register_class(StdoutPrinter)
