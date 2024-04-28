from __future__ import annotations

from ..ETKCanvas import ETKCanvas
from ..vector2d import vector2d
from .ETKUtils import gen_col_from_int
from typing import Optional
from tkinter import Tk


class ETKBackgroundCanvas(ETKCanvas):
    def __init__(self, tk: Tk, pos: vector2d, size: vector2d, background_color: int = 16777215, outline_color: Optional[int] = 0x000000) -> None:
        self.__outline_color: Optional[int] = outline_color
        ETKCanvas.__init__(self, tk, pos, size, background_color)
        self.outline_color = outline_color

    # region Properties

    @property
    def outline_color(self) -> Optional[int]:
        return self.__outline_color

    @outline_color.setter
    def outline_color(self, value: Optional[int]) -> None:
        self.__outline_color = value
        if value == None:
            self._tk_object.configure(highlightthickness=0)
        else:
            self._tk_object.configure(highlightthickness=2, highlightbackground=gen_col_from_int(value))

    # endregion