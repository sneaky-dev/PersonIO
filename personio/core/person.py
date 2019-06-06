from collections import OrderedDict


class Person(OrderedDict):
    """Person data model class.
    This is based on :obj:`OrderedDict` to maximize serialization support.

    Attributes:
        _fields(:obj:`list` of :obj:`str`): list of data keys to expect from a valid Person
    """

    _fields = [
        "last_name",
        "first_name",
        "street",
        "city",
        "zip",
        "country",
        "phone",
    ]

    def __repr__(self):
        return "<Person, '{}, {}'>".format(self.get("last_name", "Invalid"),
                                           self.get("first_name", "Invalid"))

    @classmethod
    def fields(cls):
        """Getter for ``_fields``.

        Returns:
            :obj:`list` of :obj:`str`
        """
        return cls._fields

    @classmethod
    def _validate(cls, data_dict):
        """Validates content of ``data_dict`` against ``_fields``.

        Args:
            data_dict(:obj:`dict`): dict containing person data

        Returns:
            :obj:`bool`
        """
        diff = set(cls._fields).symmetric_difference(data_dict.keys())
        if diff:
            raise ValueError("Invalid Person. "
                             "Missing or unknown values: {}".format(", ".join(diff)))
        return True

    @classmethod
    def _sort(cls, data_dict):
        """Returns sorted ``data_dict`` based on ``_fields``.

        Args:
            data_dict(:obj:`dict`): dict containing person data

        Returns:
            :obj:`dict`
        """
        return sorted(data_dict.items(), key=lambda item: cls._fields.index(item[0]))

    @classmethod
    def from_dict(cls, data_dict):
        """Creates a new ``Person`` object based on a dict containing valid person data.
        Args:
            data_dict(:obj:`dict`): dict containing person data

        Returns:
            :obj:`Person`
        """
        if cls._validate(data_dict):
            return cls(cls._sort(data_dict))

    def validate(self):
        """Validates content of this Person object.

        Returns:
            :obj:`bool`
        """
        return self._validate(self)

    def sort(self):
        """Sorts content of this Person object.
        """
        ordered = self._sort(self)
        self.clear()
        self.update(ordered)

