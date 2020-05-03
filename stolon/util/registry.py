import logging

logger = logging.getLogger("util.registry")

class _BaseRegistry(object):
    """A basic registry object to hold class references and instances."""

    available = {}
    loaded = {}

    def add(self, object_reference):
        logger.debug("adding registry object %s" % object_reference)
        if not self._validate(object_reference):
            raise TypeError("Cannot add %s to registry." % object_reference)
        if hasattr(object_reference, "NAME"):
            self.available[object_reference.NAME] = object_reference
        else:
            logger.warn("Object %s does not have NAME set, using __name__")
            self.available[object_reference.__name__] = object_reference

    def load(self, name, *args):
        logger.debug("loading registry object %s" % name)
        if name in self.loaded:
            return self.loaded[name]
        if name not in self.available:
            raise NameError("Cannot load %s from registry, object not registered" % name)
        self.loaded[name] = self.available[name](*args)
        return self.loaded[name]

    def get_available(self):
        return self.available.keys()

    def get_loaded(self):
        return self.loaded.keys()

    def _validate(self, object_reference):
        return True

class _FilterRegistry(_BaseRegistry):
    pass

FilterRegistry = _FilterRegistry()