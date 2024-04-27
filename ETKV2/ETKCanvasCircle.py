from tkinter import Canvas
from .ETKCanvasOval import ETKCanvasOval
from .vector2d import vector2d

class ETKCanvasCircle(ETKCanvasOval):
    def __init__(self, canvas: Canvas, center: vector2d, radius: int, background_color: int = 65280, outline_color: int = 0) -> None:
        ETKCanvasOval.__init__(self, canvas, center, radius, radius, background_color, outline_color)