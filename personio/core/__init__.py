from . import (
    registry,
    baseformat,
    baseprinter
)

# create new registries for formats, printers
formats = registry.Registry(baseformat.BaseFormat)
printers = registry.Registry(baseprinter.BasePrinter)
