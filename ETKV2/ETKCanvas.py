from .vector2d import vector2d
from .Internal.ETKBaseTkWidgetDisableable import ETKBaseTkWidgetDisableable
from .ETKCanvasItem import ETKCanvasItem
from .ETKCanvasRectangle import ETKCanvasRectangle
from .ETKCanvasSquare import ETKCanvasSquare
from .ETKCanvasOval import ETKCanvasOval
from .ETKCanvasCircle import ETKCanvasCircle
from .ETKCanvasLine import ETKCanvasLine
from tkinter import Canvas, Tk


class ETKCanvas(ETKBaseTkWidgetDisableable):
    def __init__(self, tk: Tk, pos: vector2d, size: vector2d, background_color: int = 0xFFFFFF) -> None:
        self._tk_object: Canvas = Canvas(tk)  # type:ignore
        ETKBaseTkWidgetDisableable.__init__(self, pos, size, background_color)

    # region Methods

    def draw_square(self, top_left: vector2d, side_length: int, background_color: int = 0xFF0000, outline_color: int = 0x000000) -> ETKCanvasItem:
        return ETKCanvasSquare(self._tk_object, top_left, side_length, background_color, outline_color)

    def draw_rect(self, top_left: vector2d, bottom_right: vector2d, background_color: int = 0xFF0000, outline_color: int = 0x000000) -> ETKCanvasItem:
        return ETKCanvasRectangle(self._tk_object, top_left, bottom_right, background_color, outline_color)

    def draw_circle(self, center: vector2d, radius: int, background_color: int = 0x00FF00, outline_color: int = 0x000000) -> ETKCanvasItem:
        return ETKCanvasCircle(self._tk_object, center, radius, background_color, outline_color)

    def draw_oval(self, center: vector2d, radius_x: int, radius_y: int, background_color: int = 0x00FF00, outline_color: int = 0x000000) -> ETKCanvasItem:
        return ETKCanvasOval(self._tk_object, center, radius_x, radius_y, background_color, outline_color)

    def draw_polygon(self, corner_list: list[vector2d], background_color: int = 0x0000FF, outline_color: int = 0x000000) -> ETKCanvasItem:
        return ETKCanvasItem(self._tk_object, corner_list, background_color, outline_color)

    def draw_line(self, start_point: vector2d, end_point: vector2d, thickness: float = 2, background_color: int = 0x000000, outline_color: int = 0x000000) -> ETKCanvasItem:
        return ETKCanvasLine(self._tk_object, start_point, end_point, thickness, background_color, outline_color)

    # endregion
