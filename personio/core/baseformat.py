from abc import ABCMeta, abstractmethod
from six import with_metaclass


class BaseFormat(with_metaclass(ABCMeta, object)):

    _label = None
    _extension = None
    _priority = 0

    def __init__(self, *args, **kwargs):
        if not self._label or not self._extension:
            raise ValueError("Invalid format configuration.")

    def read_file(self, filepath, **kwargs):
        return self._read_file(filepath=filepath,
                               **kwargs)

    def write_file(self, filepath, data, **kwargs):
        self._write_file(filepath=filepath,
                         data=data,
                         **kwargs)

    @classmethod
    def priority(cls):
        return cls._priority

    @classmethod
    def extension(cls):
        return cls._extension

    @classmethod
    def label(cls):
        return cls._label

    # Abstract

    @abstractmethod
    def _read_file(self, filepath, **kwargs):
        pass

    @abstractmethod
    def _write_file(self, filepath, data, **kwargs):
        pass
