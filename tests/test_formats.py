# unicode string for Py2 / Py3
from builtins import str as ustr

import unittest
import filecmp

from personio.core import formats as formats_registry
from personio.core import utils


class TestFormats(unittest.TestCase):

    def test_read_write(self):
        samples_dir = utils.get_resource_path("tests/test_files")
        with utils.temp_dir("rwtest") as test_dir:
            for file_format in formats_registry.list():
                filename = "persons_{name}{ext}".format(name=file_format.name().lower(),
                                                        ext=file_format.extension())
                input_filepath = samples_dir.joinpath(filename)
                output_filepath = test_dir.joinpath(filename)

                # write read sample, write to temp file
                input_data = file_format.read_file(input_filepath)
                file_format.write_file(output_filepath, input_data)

                # compare input / output file for parity
                self.assertTrue(filecmp.cmp(ustr(input_filepath),
                                            ustr(output_filepath)),
                                "Read / Write test failed for format: '{}'".format(file_format))
