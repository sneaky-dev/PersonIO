from __future__ import print_function

import argparse
import six
from . import core
import pprint

if six.PY2:
    from pathlib2 import Path
else:
    from pathlib import Path


def _get_args():
    """Parses and returns command line arguments.

    Returns:
        :obj:`dict`: parsed arguments
    """
    main_parser = argparse.ArgumentParser(description="Personal data IO tool.")
    sub_parser = main_parser.add_subparsers(title="Subcommands", help="Available subcommands", dest="command")

    # add parser
    list_parser = sub_parser.add_parser("list", description="Lists registered implementations.",
                                        help="List implementations")
    print_parser = sub_parser.add_parser("print", description="Prints data from an input file.",
                                         help="Print data from file")
    write_parser = sub_parser.add_parser("write", description="Writes data to an output file.",
                                         help="Write data to file")

    # print parser
    print_parser.add_argument("input_file", help="Input file containing the data set to be read.")
    print_parser.add_argument("printer", help="Name of the printer to be used.")
    print_parser.add_argument("-if", "--input-format", help="Name of the format to be used for reading.")

    # write parser
    write_parser.add_argument("input_file", help="Input file containing the data set to be read.")
    write_parser.add_argument("output_file", help="Output file to write the data to.")
    write_parser.add_argument("-if", "--input-format", help="Name of the format to be used for reading.")
    write_parser.add_argument("-of", "--output-format", help="Name of the format to be used for writing.")

    # list parser
    list_parser.add_argument("type", help="Type of implementation to list: formats, printers")
    list_parser.add_argument("--filter", action="append", type=lambda kv: kv.split("="), dest='filter_list')
    args = main_parser.parse_args()
    return vars(args)


def _get_format_from_filepath(filepath, preferred_format=None):
    """Extracts filepath extension and searches for matching file format in registry.

    Args:
        filepath(:obj:`basestring`): input filepath
        preferred_format(:obj:`str`, optional): preferred file format, e.g. "PrettyJSON"

    Returns:
        :obj:`BaseFormat`
    """
    file_format = core.formats.get(name=preferred_format)
    if file_format:
        return file_format

    path_obj = Path(filepath)
    file_format = core.formats.get(extension=path_obj.suffix)
    if not file_format:
        raise ValueError("Unknown file format: '{}'".format(path_obj.suffix))
    return file_format


def _run_list(**options):
    """Prints a list of registry entries.
    Can be filtered by the user.

    Args:
        **options(:obj:`dict`): filter_list, type
    """
    registries = {
        "formats": core.formats,
        "printers": core.printers,
    }

    registry_name = options.pop("type")
    if registry_name not in registries:
        raise ValueError("Invalid listing type: '{}'".format(registry_name))

    registry = registries[registry_name]
    filter_dict = dict(options.get("filter_list") or [])

    results = registry.list(**filter_dict)
    print("List results:\n{}".format(pprint.pformat(results)))


def _run_write(**options):
    """Reads an input file and writes the data to the specified output file.
    Users can specify the format by providing additional ``options``.
    Args:
        **options(:obj:`dict`): input_file, output_file, input_format, output_format

    Returns:

    """
    input_filepath = options["input_file"]
    input_format_name = options.get("input_format")
    output_filepath = options["output_file"]
    output_format_name = options.get("output_format")

    input_format = _get_format_from_filepath(input_filepath, preferred_format=input_format_name)
    output_format = _get_format_from_filepath(output_filepath, preferred_format=output_format_name)

    input_data = input_format.read_file(input_filepath)
    output_format.write_file(output_filepath, input_data)


def _run_print(**options):
    """Reads an input file and displays the data based on the specified ``printer`` option.

    Args:
        **options(:obj:`dict`): input_file, output_file, input_format, output_format

    Returns:

    """
    printer_name = options["printer"]
    input_filepath = options["input_file"]
    input_format_name = options.get("input_format")

    printer = core.printers.get(name=options["printer"])
    if not printer:
        raise ValueError("Invalid printer: '{}'".format(printer_name))

    input_format = _get_format_from_filepath(input_filepath, preferred_format=input_format_name)
    input_data = input_format.read_file(input_filepath)
    printer.print_data(input_data)


def main():
    """Application main function.
    """
    kwargs = _get_args()
    commands = {
        "list": _run_list,
        "print": _run_print,
        "write": _run_write,
    }

    command_name = kwargs.pop("command")
    commands[command_name](**kwargs)


if __name__ == '__main__':
    main()