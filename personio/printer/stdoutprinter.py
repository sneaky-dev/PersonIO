from ..core.baseprinter import BasePrinter
from .. import core


class StdoutPrinter(BasePrinter):

    _label = "Stdout"

    def _print_data(self, data, **kwargs):
        pass


# register class
core.printers.register_class(StdoutPrinter)
