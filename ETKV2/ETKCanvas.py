from .vector2d import vector2d
from .ETKBaseTkWidgetDisableable import ETKBaseTkWidgetDisableable
from .ETKUtils import gen_col_from_int
from tkinter import Canvas, Tk

class ETKCanvas(ETKBaseTkWidgetDisableable):
    def __init__(self, tk:Tk, pos: vector2d, size: vector2d, background_color: int = 0xFFFFFF) -> None:
        self._tk_object: Canvas = Canvas(tk)
        ETKBaseTkWidgetDisableable.__init__(pos, size, background_color)
    
    def draw_square(self, pos:vector2d, side_lenght:int, fill_col:int=0xFF0000, outline_col:int=0x000000, draw_mode:DrawMode = DrawMode.TOP_LEFT_CORNER)->ETKCanvasItem:
        top_left,bottom_right = self.__draw_mode_trans[draw_mode](pos,side_lenght,side_lenght)
        my_fill_col = gen_col_from_int(fill_col)
        my_outline_col = gen_col_from_int(outline_col)
        #return ETKCanvasItem(self.object_id, "square", top_left, bottom_right, my_fill_col, my_outline_col)
    
    def draw_rect(self, top_left:vector2d, bottom_right:vector2d, fill_col:int=0xFF0000, outline_col:int=0x000000)->ETKCanvasItem:
        my_fill_col = gen_col_from_int(fill_col)
        my_outline_col = gen_col_from_int(outline_col)
        #return ETKCanvasItem(self.object_id, "rectangle", top_left, bottom_right, my_fill_col, my_outline_col)
    
    def draw_circle(self, center:vector2d, radian:int, fill_col:int=0x00FF00, outline_col:int=0x000000)->ETKCanvasItem:
        my_fill_col = gen_col_from_int(fill_col)
        my_outline_col = gen_col_from_int(outline_col)
        #return ETKCanvasItem(self.object_id, "circle", center, radian, radian, my_fill_col, my_outline_col)

    def draw_oval(self, center:vector2d, radian_x:int, radian_y:int, fill_col:int=0x00FF00, outline_col:int=0x000000)->ETKCanvasItem:
        my_fill_col = gen_col_from_int(fill_col)
        my_outline_col = gen_col_from_int(outline_col)
        #return ETKCanvasItem(self.object_id, "oval", center, radian_x, radian_y, my_fill_col, my_outline_col)
    
    def draw_polygon(self, corner_list:list[vector2d], fill_col:int=0x0000FF, outline_col:int=0x000000)->ETKCanvasItem:
        my_fill_col = gen_col_from_int(fill_col)
        my_outline_col = gen_col_from_int(outline_col)
        #return ETKCanvasItem(self.object_id, "polygon", corner_list, my_fill_col, my_outline_col)
    
    def draw_line(self, pos1:vector2d, pos2:vector2d, line_col:int=0x000000, line_thickness:int=2)->ETKCanvasItem:
        my_fill_col = gen_col_from_int(line_col)
        #return ETKCanvasItem(self.object_id, "line", [pos1, pos2], my_fill_col, line_thickness)