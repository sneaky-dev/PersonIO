"""Utility module.
"""

# unicode string for Py2 / Py3
from builtins import str as ustr

import contextlib
import shutil
import sys

import six

if six.PY2:
    from pathlib2 import Path
else:
    from pathlib import Path


@contextlib.contextmanager
def temp_dir(directory_name):
    """Context manager providing a temp directory that will be deleted on exit.
    Args:
        directory_name(:obj:`str`): directory name
    """
    dir_path = Path.home().joinpath("tmp", "personio", directory_name)
    try:
        dir_path.mkdir(parents=True, exist_ok=True)
        yield dir_path
    finally:
        if dir_path.exists():
            shutil.rmtree(ustr(dir_path))


@contextlib.contextmanager
def stdout_to_file(filepath):
    """Context manager redirecting stdout data to a file descriptor.

    Args:
        filepath(:obj:`str`): filepath to redirect output to
    """
    filepath_obj = Path(filepath)
    filepath_obj.parent.mkdir(parents=True, exist_ok=True)

    orig_stdout = sys.stdout
    try:
        with filepath_obj.open("wb+" if six.PY2 else "w+") as file_obj:
            sys.stdout = file_obj
            yield
    finally:
        sys.stdout = orig_stdout


def get_resource_path(rel_path):
    """Returns the absolute path to a file or directory relative to the repository root.

    Args:
        rel_path(:obj:`str`): path relative to repository root

    Returns:
        :obj:`Path`
    """
    root_dir = Path(__file__).parents[2]
    return root_dir.joinpath(rel_path)