from tkinter import Widget as tk_widget

from .ETKUtils import gen_col_from_int

from ..vector2d import vector2d
from .ETKBaseWidget import ETKBaseWidget
from .ETKBaseTkObject import ETKBaseTkObject


class ETKBaseTkWidget(ETKBaseTkObject, ETKBaseWidget):

    def __init__(self, pos: vector2d, size: vector2d, background_color: int) -> None:
        self._tk_object: tk_widget
        ETKBaseWidget.__init__(self, pos, size, background_color)
        ETKBaseTkObject.__init__(self, pos, size, background_color)
        self.__place_object()

    # region Properties

    @ETKBaseWidget.size.setter
    def size(self, value: vector2d) -> None:
        ETKBaseWidget.size.fset(self, value)  # type:ignore
        self.__place_object()

    @property
    def outline_color(self) -> int:
        return int(self._outline_color[1:], 16)

    @outline_color.setter
    def outline_color(self, value: int) -> None:
        col = gen_col_from_int(value)
        self._outline_color = col
        self._tk_object.configure(highlightbackground=col)  # type:ignore

    @property
    def outline_thickness(self) -> int:
        return self._outline_thickness

    @outline_thickness.setter
    def outline_thickness(self, value: int) -> None:
        self._outline_thickness = value
        self._tk_object.configure(highlightthickness=value)  # type:ignore

    # endregion
    # region Methods

    def __place_object(self) -> None:
        pos = self.abs_pos
        self._tk_object.place(
            x=pos.x, y=pos.y, width=self._size.x, height=self._size.y)

        # region update event methods

    def _update_pos(self) -> None:
        self.__place_object()

    def _update_visibility(self) -> None:
        if self.abs_visibility:
            self.__place_object()
        else:
            self._tk_object.place_forget()

    # endregion
    # endregion
