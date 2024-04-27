from .vector2d import vector2d
from .ETKBaseWidget import ETKBaseWidget


class ETKBaseWidgetDisableable(ETKBaseWidget):
    def __init__(self, pos: vector2d, size: vector2d) -> None:
        ETKBaseWidget.__init__(self, pos, size)

    @ETKBaseWidget.enabled.setter
    def enabled(self, value: bool) -> None:
        """ """
        self._enabled = value
