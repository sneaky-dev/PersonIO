from __future__ import print_function

from abc import ABCMeta, abstractmethod
from six import with_metaclass


class BasePrinter(with_metaclass(ABCMeta, object)):

    _name = None
    _priority = 0

    def __init__(self, *args, **kwargs):
        if not self._name:
            raise ValueError("Invalid printer configuration.")

    def __repr__(self):
        return "<{}, Name: '{}' (Priority: {})>".format(type(self).__name__, self.name(), self.priority())

    def print_data(self, data, **kwargs):
        print("Print data using '{}' printer ...".format(self.name()))
        self._print_data(data)

    @classmethod
    def priority(cls):
        return cls._priority

    @classmethod
    def name(cls):
        return cls._name

    # Abstract

    @abstractmethod
    def _print_data(self, data, **options):
        pass
