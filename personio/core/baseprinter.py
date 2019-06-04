from abc import ABCMeta, abstractmethod
from six import with_metaclass


class BasePrinter(with_metaclass(ABCMeta, object)):

    _label = None
    _priority = 0

    def __init__(self, *args, **kwargs):
        if not self._extension:
            raise ValueError("Invalid printer configuration.")

    def print_data(self, data, **kwargs):
        pass

    @classmethod
    def priority(cls):
        return cls._priority

    @classmethod
    def label(cls):
        return cls._label

    # Abstract

    @abstractmethod
    def _print_data(self, data, **kwargs):
        pass
