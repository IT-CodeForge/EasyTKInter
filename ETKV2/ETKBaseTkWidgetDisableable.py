from ETKV2.vector2d import vector2d
from .ETKBaseTkWidget import ETKBaseTkWidget
from .ETKBaseWidgetDisableable import ETKBaseWidgetDisableable

class ETKBaseTkWidgetDisableable(ETKBaseWidgetDisableable, ETKBaseTkWidget):
    def __init__(self, pos: vector2d, size: vector2d, background_color: int = 0xAAAAAA) -> None:
        ETKBaseTkWidget.__init__(self, pos, size, background_color)
        ETKBaseWidgetDisableable.__init__(self, pos, size)
        

    @ETKBaseWidgetDisableable.enabled.setter
    def enabled(self, value: bool) -> None:
        ETKBaseWidgetDisableable.enabled.fset(self, value) #type:ignore
        if self._enabled:
            self._tk_object["state"] = "normal"
        else:
            self._tk_object["state"] = "disabled"