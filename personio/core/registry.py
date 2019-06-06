# unicode string for Py2 / Py3
from builtins import str as ustr


class Registry(object):
    """Implementation registry.
    Serves register for implementation classes and as factory for format / printer instances.
    """

    def __init__(self, base_cls):
        """Init.

        Args:
            base_cls(:obj:`class`): base class for registry
        """
        self._base_cls = base_cls
        self._classes = set()
        self._class_instances = {}

    def __repr__(self):
        return "<Registry, '{}' (Items: '{}')>".format(self._base_cls, len(self._classes))

    def _get_instance(self, cls):
        if cls not in self._class_instances:
            self._class_instances[cls] = cls()
        return self._class_instances[cls]

    def register_class(self, cls):
        """Registers a class with this registry object, if the class wasn't registered yet.
        The class needs to be a subclass of ``_baseclass``

        Args:
            cls(:obj:`class`): class to register
        """
        if not issubclass(cls, self._base_cls):
            raise ValueError("Cannot register class. Invalid type: '{}'.".format(cls))
        self._classes.add(cls)

    def list(self, **filter):
        """Lists registered classes.
        Output can be filtered by supplying filter options via ``filter``

        Args:
            **filter(:obj:`dict`): filters classes based on class members / values, e.g. "name" == "JSON"

        Returns:
            :obj:`list` of :obj:`class`
        """
        results = list(self._classes)
        for item in self._classes:
            for attr, filter_value in filter.items():
                item_value = getattr(item, attr, "")
                if callable(item_value):
                    item_value = item_value()
                if ustr(item_value).lower() != ustr(filter_value).lower():
                    results.remove(item)
        return [self._get_instance(cls) for cls in results]

    def get(self, **filter):
        """Returns the class with the highest priority matching the ``filter`` options.

        Args:
            **filter(:obj:`dict`): filters classes based on class members / values, e.g. "name" == "JSON"

        Returns:
            :obj:`class`
        """
        sorted_list = sorted(self.list(**filter), key=lambda x: x.priority(), reverse=True)
        return next(iter(sorted_list), None)
