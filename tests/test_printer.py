# unicode string for Py2 / Py3
from builtins import str as ustr

import unittest
import filecmp

from personio.core import printers as printers_registry
from personio.core import utils
from personio.core import formats as formats_registry


class TestPrinters(unittest.TestCase):
    """Unit tests for the file format implementations.
    The tests are performed by comparing the output of the printer against a target file.
    """

    def test_stdout_printer(self):
        """Tests the Stdout table printer.
        """
        target_filepath = utils.get_resource_path("tests/test_files/persons_stdout.txt")
        input_filepath = utils.get_resource_path("tests/test_files/persons_json.json")
        file_format = formats_registry.get(extension=input_filepath.suffix)
        printer = printers_registry.get(name="Stdout")

        input_data = file_format.read_file(input_filepath)
        with utils.temp_dir("printtest") as temp_dir:
            test_filepath = temp_dir.joinpath("persons_stdout.txt")
            with utils.stdout_to_file(test_filepath):
                printer.print_data(input_data)

            # compare input / output file for parity
            self.assertTrue(filecmp.cmp(ustr(test_filepath), ustr(target_filepath)))

    def test_html_printer(self):
        """Tests the HTML printer.
        """
        target_filepath = utils.get_resource_path("tests/test_files/persons_html.html")
        input_filepath = utils.get_resource_path("tests/test_files/persons_json.json")
        file_format = formats_registry.get(extension=input_filepath.suffix)
        printer = printers_registry.get(name="HTML")

        # read / write data
        input_data = file_format.read_file(input_filepath)
        printer.print_data(input_data)

        # compare input / output file for parity
        self.assertTrue(filecmp.cmp(ustr(printer.temp_filepath), ustr(target_filepath)))

