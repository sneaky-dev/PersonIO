class Registry(object):

    def __init__(self, base_cls):
        self._base_cls = base_cls
        self._classes = set()

    def __repr__(self):
        return "<Registry, '{}' (Items: '{}')>".format(self._base_cls, len(self._classes))

    def register_class(self, cls):
        if not issubclass(cls, self._base_cls):
            raise ValueError("Cannot register class. Invalid type: '{}'.".format(cls))
        self._classes.add(cls)

    def list(self, **filter):
        results = list(self._classes)
        for item in self._classes:
            for attr, filter_value in filter.items():
                item_value = getattr(item, attr, None)
                if callable(item_value):
                    item_value = item_value()
                if item_value != filter_value:
                    results.remove(item)
        return results

    def get(self, **filter):
        sorted_list = sorted(self.list(**filter), key=lambda x: x.priority(), reverse=True)
        return next(iter(sorted_list), None)
