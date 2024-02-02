from tkinter  import Canvas
from vector2d import vector2d
import math

#types: "line" "rectangle" "square" "oval" "circle" "polygon"

class TGCanvasItem:
    def __init__(self, canvas:Canvas, item_type:str, *args) -> None:
        self.__my_Canvas = canvas
        self.__item_type = item_type
        if type(args[0]) == vector2d:
            self.__anchor = args[0]
        elif type(args[0]) == list:
            self.__anchor = args[0][0]
        self.item_id = 0
        if item_type == "line":
            self.__gen_line(*args)
            self.__point_list = [args[0].x, args[0].y, args[1].x, args[1].y]
            return
        self.__point_list = self.__generate_pointlist(*args[:-2])
        self.__make_shape(self.__point_list, *args[-2:])
    
    @property
    def anchor(self)->vector2d:
        return self.__anchor
    
    @anchor.setter
    def anchor(self, value:vector2d):
        self.__anchor = value


    def __generate_pointlist(self, *args):
        if self.__item_type in ["oval", "circle"]:
            self.anchor  = args[0]
            return self.__poly_oval(*args)
        if self.__item_type in ["rectangle", "square"]:
            return self.__poly_quad(*args)
        if self.__item_type == "polygon":
            return self.__point_unpacking(*args)

    def __poly_oval(self, center:vector2d, radian_x:int, radian_y:int, rotation_in_radians:float=0):
        steps = int((radian_x + radian_y) / 4)
        point_list = []
        theta = 0
        for i in range(steps):
            my_point = center + vector2d(radian_x * math.cos(theta), radian_y * math.sin(theta)).rotate(rotation_in_radians)
            point_list.append(my_point.x)
            point_list.append(my_point.y)
            theta += (2*math.pi) / steps
        return point_list

    def __poly_quad(self, top_left:vector2d, bottom_right:vector2d, rotation_in_radians:float=0):
        vec_list = [top_left, vector2d(bottom_right.x, top_left.y), bottom_right, vector2d(top_left.x, bottom_right.y)]
        vec_list_fin = [point.rotate(rotation_in_radians) for point in vec_list]
        return self.__point_unpacking(vec_list_fin)

    def __point_unpacking(self, vec_list:list[vector2d])->list[float]:
        getx = lambda vec: vec.x
        gety = lambda vec: vec.y
        return [f(point) for point in vec_list for f in (getx, gety)]
    
    def __gen_line(self, pos1:vector2d, pos2:vector2d, fill:str, line_thickness:int):
        self.item_id = self.__my_Canvas.create_line(pos1.x, pos1.y, pos2.x, pos2.y, fill=fill, width=line_thickness)
    
    def __make_shape(self,pointlist:list[float], fill:str, outline:str):
        self.item_id = self.__my_Canvas.create_polygon(pointlist, fill=fill, outline=outline)
    
    def rotate_with_radians(self, radians:float):
        coords = self.__my_Canvas.coords(self.item_id)
        vec_list = [self.__anchor + (vector2d(coords[index*2], coords[index*2+1]) - self.__anchor).rotate(radians) for index in range(len(coords)//2)]
        self.__point_list = self.__point_unpacking(vec_list)
        self.__my_Canvas.coords(self.item_id, self.__point_list)
    
    def rotate_with_degrees(self, degrees:float):
        self.rotate_with_radians(degrees * math.pi / 180)

    
    def move(self, mov_vec:vector2d):
        self.__my_Canvas.move(self.item_id, mov_vec.x, mov_vec.y)

    def move_to(self, pos:vector2d):
        for index, x_or_y in enumerate(self.__point_list):
            if index%2:
                self.__point_list[index] = x_or_y - self.anchor.y + pos.y
            else:
                self.__point_list[index] = x_or_y - self.anchor.x + pos.x
        self.anchor = pos
        self.__my_Canvas.coords(self.item_id, self.__point_list)