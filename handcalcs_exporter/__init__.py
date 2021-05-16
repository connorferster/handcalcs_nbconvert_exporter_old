__version__ = "0.1.0"

import os
import traitlets
from nbconvert.exporters import HTMLExporter

class HandCalcsExporter(HTMLExporter):
    """
    Exports to HTML. Input cells and all tags are removed.
    """
    export_from_notebook = "handcalcs HTML"

    @property
    def template_paths(self):
        paths = super()._template_paths()+[os.path.join(os.path.dirname(__file__), "templates")]
        return paths

