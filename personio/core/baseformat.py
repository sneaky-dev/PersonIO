from __future__ import print_function

from abc import ABCMeta, abstractmethod
from collections import Iterable
from .person import Person
import six

if six.PY2:
    from pathlib2 import Path
else:
    from pathlib import Path


class BaseFormat(six.with_metaclass(ABCMeta, object)):
    _name = None
    _extension = None
    _priority = 0

    def __init__(self, *args, **kwargs):
        if not self._name or not self._extension:
            raise ValueError("Invalid format configuration.")

    def __repr__(self):
        return "<{}, Name: '{}' (Ext.: '{}', Priority: {})>".format(type(self).__name__,
                                                                    self.name(),
                                                                    self.extension(),
                                                                    self.priority())

    def read_file(self, filepath, **kwargs):
        path_obj = Path(filepath)
        if not path_obj.exists():
            raise ValueError("Cannot read file. Invalid filepath: '{}'".format(path_obj))
        print("Read file with format '{}': '{}'".format(self.name(), filepath))
        return [Person.from_dict(x) for x in self._read_file(filepath=path_obj, **kwargs)]

    def write_file(self, filepath, data, **kwargs):
        if not isinstance(data, Iterable):
            raise ValueError("Cannot write data. Data is not a valid iterable: '{}'".format(type(data)))

        # create mising directories
        path_obj = Path(filepath)
        path_obj.parent.mkdir(parents=True, exist_ok=True)

        print("Write data to file with format '{}': '{}'".format(self.name(), filepath))
        self._write_file(filepath=path_obj, data=data, **kwargs)

    @classmethod
    def priority(cls):
        return cls._priority

    @classmethod
    def extension(cls):
        return cls._extension

    @classmethod
    def name(cls):
        return cls._name

    # Abstract

    @abstractmethod
    def _read_file(self, filepath, **options):
        pass

    @abstractmethod
    def _write_file(self, filepath, data, **options):
        pass
