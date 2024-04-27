import math
from .ETKCanvasItem import ETKCanvasItem
from tkinter import Canvas
from .vector2d import vector2d

class ETKCanvasLine(ETKCanvasItem):
    def __init__(self, canvas: Canvas, start_point: vector2d, end_point:vector2d, thickness: float, background_color: int, outline_color: int) -> None:
        direction_vector = end_point - start_point
        thickness_vector = direction_vector.rotate(0.5*math.pi).normalize() * 0.5 * thickness
        temp_pointlist: list[vector2d] = [start_point + thickness_vector, end_point + thickness_vector, start_point - thickness_vector, end_point - thickness_vector]
        super().__init__(canvas, temp_pointlist, background_color, outline_color)
    
    @ETKCanvasItem.pos.getter
    def pos(self)->vector2d:
        return 0.5 * (self._pointlist[0] + self._pointlist[-1])