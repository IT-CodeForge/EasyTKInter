from ..ETKCanvas import ETKCanvas
from ..vector2d import vector2d
from typing import Optional
from tkinter import Tk


class ETKBackgroundCanvas(ETKCanvas):
    def __init__(self, tk: Tk, pos: vector2d, size: vector2d, background_color: int = 16777215, outline_color: Optional[int] = 0x000000) -> None:
        ETKCanvas.__init__(self, tk, pos, size, background_color)
        if outline_color == None:
            my_outline = background_color
        else:
            my_outline: int = outline_color
        self.__background_and_outline = self.draw_rect(
            vector2d(), size, background_color, my_outline)

    # region Properties

    @ETKCanvas.background_color.setter
    def background_color(self, value: Optional[int]) -> None:
        ETKCanvas.background_color.fset(self, value)  # type:ignore
        if getattr(self, "__background_and_outline", None) != None:
            self.__background_and_outline.background_color = value

    @property
    def outline_color(self) -> int:
        return self.__background_and_outline.outline_color

    @outline_color.setter
    def outline_color(self, value: int) -> None:
        self.__background_and_outline.outline_color = value

    # endregion
