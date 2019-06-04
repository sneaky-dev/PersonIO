

class Person(dict):

    _attrs = [
        "first_name",
        "last_name",
        "street",
        "city",
        "zip",
        "phone",
    ]

    def validate(self):
        for attr in self._attrs:
            if attr not in self:
                raise ValueError("Invalid Person. Missing value for '{}'".format(attr))
        return True
