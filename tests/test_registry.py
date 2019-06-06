import unittest

from personio.core import formats as formats_registry
from personio.core import printers as printers_registry

from personio.format.csvformat import CSVFormat
from personio.format.jsonformat import JSONFormat
from personio.format.prettyjsonformat import PrettyJSONFormat
from personio.printer.htmlprinter import HTMLPrinter
from personio.printer.stdoutprinter import StdoutPrinter


class TestRegistry(unittest.TestCase):

    def test_registered_formats(self):
        expected = {CSVFormat, JSONFormat, PrettyJSONFormat}
        registered = {type(x) for x in formats_registry.list()}
        self.assertEqual(registered, expected)

    def test_registered_printers(self):
        expected = {HTMLPrinter, StdoutPrinter}
        registered = {type(x) for x in printers_registry.list()}
        self.assertEqual(registered, expected)

    def test_filter_formats(self):
        self.assertEqual({type(x) for x in formats_registry.list(priority=100)}, {JSONFormat})
        self.assertEqual({type(x) for x in formats_registry.list(extension=".json")}, {JSONFormat, PrettyJSONFormat})
        self.assertEqual(type(formats_registry.get(extension=".json")), JSONFormat)
        self.assertEqual(type(formats_registry.get(name="JSON")), JSONFormat)

    def test_filter_printers(self):
        self.assertEqual({type(x) for x in printers_registry.list(priority=0)}, {StdoutPrinter, HTMLPrinter})
        self.assertEqual({type(x) for x in printers_registry.list(name="HTML")}, {HTMLPrinter})
