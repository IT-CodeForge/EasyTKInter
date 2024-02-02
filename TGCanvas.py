from tkinter import Canvas, Tk
from TGBaseWidget import TGBaseWidget
from vector2d import vector2d
from enum import Enum
from TGCanvasItem import TGCanvasItem
from typing import Callable, Final
import math

class DrawMode(Enum):
    TOP_LEFT_CORNER: Final = 0,
    CENTER: Final = 1,
    BOTTOM_RIGHT_CORNER: Final = 2

class TGCanvas(TGBaseWidget):
    def __init__(self, myTk:Tk, posX:int, posY:int, width:int = 100, height:int = 100) -> None:
        self.object_id:Canvas = Canvas(myTk)
        super().__init__(vector2d(posX, posY), vector2d(width, height))
        self.__draw_mode_trans = {
                        DrawMode.TOP_LEFT_CORNER:lambda pos, width, height : [pos,pos+vector2d(width, height)],
                        DrawMode.BOTTOM_RIGHT_CORNER:lambda pos, width, height : [pos,pos-vector2d(width, height)],
                        DrawMode.CENTER:lambda pos, width, height : [pos-vector2d(width/2, height/2),pos+vector2d(width/2, height/2)]}
    
    def draw_square(self, pos:vector2d, side_lenght:int, fill_col:int=0xFF0000, outline_col:int=0x000000, draw_mode:DrawMode = DrawMode.TOP_LEFT_CORNER)->TGCanvasItem:
        top_left,bottom_right = self.__draw_mode_trans[draw_mode](pos,side_lenght,side_lenght)
        my_fill_col = self.__gen_col_from_int(fill_col)
        my_outline_col = self.__gen_col_from_int(outline_col)
        return TGCanvasItem(self.object_id, "square", top_left, bottom_right, my_fill_col, my_outline_col)
    
    def draw_rect(self, pos:vector2d, width:int, height:int, fill_col:int=0xFF0000, outline_col:int=0x000000, draw_mode:DrawMode = DrawMode.TOP_LEFT_CORNER)->TGCanvasItem:
        top_left,bottom_right = self.__draw_mode_trans[draw_mode](pos,width,height)
        my_fill_col = self.__gen_col_from_int(fill_col)
        my_outline_col = self.__gen_col_from_int(outline_col)
        return TGCanvasItem(self.object_id, "rectangle", top_left, bottom_right, my_fill_col, my_outline_col)
    
    def draw_rect(self, top_left:vector2d, bottom_right:vector2d, fill_col:int=0xFF0000, outline_col:int=0x000000)->TGCanvasItem:
        my_fill_col = self.__gen_col_from_int(fill_col)
        my_outline_col = self.__gen_col_from_int(outline_col)
        return TGCanvasItem(self.object_id, "rectangle", top_left, bottom_right, my_fill_col, my_outline_col)
    
    def draw_circle(self, center:vector2d, radian:int, fill_col:int=0x00FF00, outline_col:int=0x000000)->TGCanvasItem:
        my_fill_col = self.__gen_col_from_int(fill_col)
        my_outline_col = self.__gen_col_from_int(outline_col)
        return TGCanvasItem(self.object_id, "circle", center, radian, radian, my_fill_col, my_outline_col)

    def draw_oval(self, center:vector2d, radian_x:int, radian_y:int, fill_col:int=0x00FF00, outline_col:int=0x000000)->TGCanvasItem:
        my_fill_col = self.__gen_col_from_int(fill_col)
        my_outline_col = self.__gen_col_from_int(outline_col)
        return TGCanvasItem(self.object_id, "oval", center, radian_x, radian_y, my_fill_col, my_outline_col)
    
    def draw_polygon(self, corner_list:list[vector2d], fill_col:int=0x0000FF, outline_col:int=0x000000)->TGCanvasItem:
        my_fill_col = self.__gen_col_from_int(fill_col)
        my_outline_col = self.__gen_col_from_int(outline_col)
        return TGCanvasItem(self.object_id, "polygon", corner_list, my_fill_col, my_outline_col)
    
    def draw_line(self, pos1:vector2d, pos2:vector2d, line_col:int=0x000000, line_thickness:int=2)->TGCanvasItem:
        my_fill_col = self.__gen_col_from_int(line_col)
        return TGCanvasItem(self.object_id, "line", pos1, pos2, my_fill_col, line_thickness)
        

    def __gen_col_from_int(self, col:int)->str:
        hold_str = hex(col)[2:]
        if len(hold_str) < 6:
            hold_str = "0"*(6-len(hold_str)) + hold_str
        return "#" + hold_str