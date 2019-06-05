from collections import OrderedDict


class Person(OrderedDict):

    _fields = [
        "last_name",
        "first_name",
        "street",
        "city",
        "zip",
        "country",
        "phone",
    ]

    @classmethod
    def fields(cls):
        return cls._fields

    @classmethod
    def _validate(cls, data_dict):
        diff = set(cls._fields).symmetric_difference(data_dict.keys())
        if diff:
            raise ValueError("Invalid Person. "
                             "Missing or unknown values: {}".format(", ".join(diff)))
        return True

    @classmethod
    def _sort(cls, data_dict):
        return sorted(data_dict.items(), key=lambda item: cls._fields.index(item[0]))

    @classmethod
    def from_dict(cls, data_dict):
        if cls._validate(data_dict):
            return cls(cls._sort(data_dict))

    def validate(self):
        return self._validate(self)

    def sort(self):
        ordered = self._sort(self)
        self.clear()
        self.update(ordered)

