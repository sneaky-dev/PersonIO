from ..core.baseprinter import BasePrinter
from .. import core


class HTMLPrinter(BasePrinter):

    _label = "HTML"

    def _print_data(self, data, **kwargs):
        pass


# register class
core.printers.register_class(HTMLPrinter)
