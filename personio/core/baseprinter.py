from __future__ import print_function

from abc import ABCMeta, abstractmethod
from six import with_metaclass


class BasePrinter(with_metaclass(ABCMeta, object)):
    """Abstract base class for a printer.

    Attributes:
        _name(:obj`str`): printer name, e.g. "HTML"
        _priority(:obj:`int`): printer priority value
    """

    _name = None
    _priority = 0

    def __init__(self, *args, **kwargs):
        if not self._name:
            raise ValueError("Invalid printer configuration.")

    def __repr__(self):
        return "<{}, Name: '{}' (Priority: {})>".format(type(self).__name__, self.name(), self.priority())

    def print_data(self, data, **kwargs):
        """Displays data, depending on implementation.

        Args:
            data(:obj:`list` of :obj:`Person`): list of persons to display
            **kwargs: unused placeholder
        """
        print("Print data using '{}' printer ...".format(self.name()))
        self._print_data(data)

    @classmethod
    def priority(cls):
        """Getter for ``_priority``

        Returns:
            :obj:`int`
        """
        return cls._priority

    @classmethod
    def name(cls):
        """Getter for ``_name``

        Returns:
            :obj:`str`
        """
        return cls._name

    # Abstract

    @abstractmethod
    def _print_data(self, data, **options):
        """Abstract print function.
        Subclasses need to implement their printing functionality here.

        Args:
            data(:obj:`list` of :obj:`Person`): list of persons to display
            **options(:obj:`dict`): unused options placeholder
        """
        pass
