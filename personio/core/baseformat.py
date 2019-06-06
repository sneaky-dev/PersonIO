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
    """Abstract base class for a file format.

    Attributes:
        _name(:obj`str`): printer name, e.g. "HTML"
        _extension(:obj:`str`): file extension representing the format
        _priority(:obj:`int`): printer priority value
    """
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
        """Reads file at ``filepath``, deserializes data and returns it as :obj:`Person` objects.

        Args:
            filepath(:obj:`str`): input filepath
            **kwargs(:obj:`dict`): unused placeholder

        Returns:
            :obj:`list` of :obj:`Person`
        """
        path_obj = Path(filepath)
        if not path_obj.exists():
            raise ValueError("Cannot read file. Invalid filepath: '{}'".format(path_obj))
        print("Read file with format '{}': '{}'".format(self.name(), filepath))
        return [Person.from_dict(x) for x in self._read_file(filepath=path_obj, **kwargs)]

    def write_file(self, filepath, data, **kwargs):
        """Serializes ``data`` and writes it to ``filepath``.

        Args:
            filepath(:obj:`str`): input filepath
            data(:obj:`list` of :obj:`Person`): list of person data to serialize
            **kwargs(:obj:`dict`): unused placeholder
        """
        if not isinstance(data, Iterable):
            raise ValueError("Cannot write data. Data is not a valid iterable: '{}'".format(type(data)))

        # create mising directories
        path_obj = Path(filepath)
        path_obj.parent.mkdir(parents=True, exist_ok=True)

        print("Write data to file with format '{}': '{}'".format(self.name(), filepath))
        self._write_file(filepath=path_obj, data=data, **kwargs)

    @classmethod
    def priority(cls):
        """Getter for ``_priority``

        Returns:
            :obj:`int`
        """
        return cls._priority

    @classmethod
    def extension(cls):
        """Getter for ``_extension``

        Returns:
            :obj:`str`
        """
        return cls._extension

    @classmethod
    def name(cls):
        """Getter for ``_name``

        Returns:
            :obj:`str`
        """
        return cls._name

    # Abstract

    @abstractmethod
    def _read_file(self, filepath, **options):
        """Abstract file reading implementation.
        Subclasses need to implement their reading functionality here.

        Args:
            filepath(:obj:`Path`): input filepath
            **options: unused placeholder

        Returns:
            :obj:`list` of :obj:`dict`
        """
        pass

    @abstractmethod
    def _write_file(self, filepath, data, **options):
        """Abstract file reading implementation.
        Subclasses need to implement their reading functionality here.

        Args:
            filepath(:obj:`Path`): output filepath
            data(:obj:`list` of :obj:`Person`): list of person data to serialize
            **options: unused placeholder
        """
        pass
