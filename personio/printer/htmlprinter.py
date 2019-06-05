# unicode string for Py2 / Py3
from builtins import str as ustr

from ..core.person import Person
from ..core.baseprinter import BasePrinter
from .. import core

import six
import webbrowser

if six.PY2:
    from pathlib2 import Path
else:
    from pathlib import Path


class HTMLPrinter(BasePrinter):

    _name = "HTML"

    def _print_data(self, data, **options):
        # generate HTML code
        header_titles = Person.fields()
        html_str = '<table>\n<tr><th>{}</th></tr>\n'.format('</th><th>'.join(header_titles))
        for item in [item.values() for item in data]:
            html_str += '<tr><td>{}</td></tr>\n'.format('</td><td>'.join(item))
        html_str += '</table>'

        # write HTML code to file
        filepath = Path.home().joinpath("tmp", "personio_tmp.html")
        print("Write temp HTML file and open it in webbrowser: '{}'".format(filepath))
        filepath.parent.mkdir(parents=True, exist_ok=True)
        filepath.write_text(ustr(html_str))

        # open in webbrowser
        webbrowser.open(filepath.as_uri())


# register class
core.printers.register_class(HTMLPrinter)
