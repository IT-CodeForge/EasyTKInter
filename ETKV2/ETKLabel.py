from tkinter import END, Text, Tk
from .vector2d import vector2d
from .Internal.ETKBaseTkWidgetText import ETKBaseTkWidgetText


class ETKLabel(ETKBaseTkWidgetText):
    def __init__(self, tk: Tk, text: str, pos: vector2d = vector2d(0, 0), size: vector2d = vector2d(80, 17), background_color: int = 11184810, text_color: int = 0) -> None:
        self._tk_object: Text = Text(tk)  # type:ignore
        ETKBaseTkWidgetText.__init__(
            self, text, pos, size, background_color, text_color)
        self._tk_object["state"] = "disabled"

    # region Properties

    @property
    def text(self) -> str:
        return self._tk_object.get("1.0", 'end-1c')

    @text.setter
    def text(self, value: str) -> None:
        self._tk_object.delete(1.0, END)
        self._tk_object.insert(1.0, value)

    # endregion
