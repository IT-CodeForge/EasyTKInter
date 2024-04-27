from __future__ import annotations
from .ETKUtils import gen_col_from_int
from tkinter import Canvas
from typing import Callable, Optional
from.vector2d import vector2d

class ETKCanvasItem:
    def __init__(self, canvas:Canvas, pointlist:list[vector2d], background_color:int, outline_color:int) -> None:
        self._tk_object: Canvas = canvas
        self._pointlist: list[vector2d] = pointlist
        self._rotation: float = 0
        self._background_color: str = gen_col_from_int(background_color)
        self._outline_color: str = gen_col_from_int(outline_color)
        tkinter_pointlist: list[tuple[float,float]] = [(vector.x, vector.y) for vector in self._pointlist]
        self.itemId: int = self._tk_object.create_polygon(coords=tkinter_pointlist, fill=self._background_color, outline=self._outline_color) #type:ignore

    @property
    def pos(self)->vector2d:
        return self._pointlist[0]
    
    @pos.setter
    def pos(self, value: vector2d)->None:
        move_vec = value - self.pos
        for index, point in enumerate(self._pointlist):
            self._pointlist[index] = point + move_vec
        self._transform_shape()
    
    @property
    def rotation(self)->float:
        return self._rotation
    
    @rotation.setter
    def rotation(self, value: float)->None:
        self._rotation = value
        for index, point in enumerate(self._pointlist):
            self._pointlist[index] = self.pos + (point - self.pos).rotate(self.rotation)
        self._transform_shape()
    
    @property
    def background_color(self)->int:
        return int(self._background_color[1:], 16)
    
    @background_color.setter
    def background_color(self, value: int)->None:
        self._background_color = gen_col_from_int(value)
        self.__redraw_shape()
    
    @property
    def outline_color(self)->int:
        return int(self._outline_color[1:], 16)
    
    @outline_color.setter
    def outline_color(self, value: int)->None:
        self._outline_color = gen_col_from_int(value)
        self.__redraw_shape()
    
    def find_intersections(self, shape: ETKCanvasItem)->list[vector2d]:
        solution_list: list[vector2d] = []
        other_pointlist = shape._pointlist + [shape._pointlist[0]]
        my_pointlist = self._pointlist + [self._pointlist[0]]
        for i in range(len(my_pointlist) - 1):
            for n in range(len(other_pointlist) - 1):
                p1 = my_pointlist[i]
                p2 = my_pointlist[i + 1]
                p3 = other_pointlist[n]
                p4 = other_pointlist[n + 1]
                intersection = self.__find_intersection(p1, p2, p3, p4)
                if intersection != None and intersection not in solution_list:
                    solution_list.append(intersection)
        return solution_list
    
    def is_point_in_shape(self, point: vector2d)->bool:
        solution = self. __winding_numbers(point)
        if solution == 0:
            return False
        else:
            return True
    
    def __winding_numbers(self, point:vector2d):
        direction_vec: vector2d = vector2d(1,0)
        p3 = point
        x_list = [vector.x for vector in self._pointlist]
        y_list = [vector.y for vector in self._pointlist]
        distance_to_bounding_box = vector2d(max(x_list), min(y_list))
        
        retval = 0.0

        p4 = point + direction_vec.normalize() * distance_to_bounding_box
        for index in range(len(self._pointlist)):
            p1 = vector2d(self._pointlist[index].x, self._pointlist[index].y)
            p2 = vector2d(self._pointlist[index + 1].x, self._pointlist[index + 1].y)
            sol = self.__find_intersection(p1,p2,p3,p4)
            if sol == None:
                continue
            poly_edge_dir = p2 - p1
            sign = (poly_edge_dir*vector2d(0,1)).normalize().y
            if sign not in [-1,1]:
                print((poly_edge_dir*vector2d(0,1)).normalize())
            if sol in [p1,p2]:
                retval += 0.5 * sign
            else:
                retval += sign
            
        return retval
    
    def __find_intersection(self, p1:vector2d, p2:vector2d, p3:vector2d, p4:vector2d)->Optional[vector2d]:
        s1 = p2 - p1
        s2 = p4 - p3

        denominator = s1.crossproduct(s2)

        if denominator == 0:
            return None

        s = p3 - p1
        t = s.crossproduct(s2) / denominator
        u = s.crossproduct(s1) / denominator

        if 0 <= t <= 1 and 0 <= u <= 1:
            intersection = p1 + t * s1
            return intersection
        else:
            return None

    def _transform_shape(self)->None:
        tkinter_pointlist: list[float] = self.__get_tkinter_pointlist()
        self._tk_object.coords(self.itemId, tkinter_pointlist)

    def __redraw_shape(self)->None:
        self._tk_object.delete(self.itemId)
        tkinter_pointlist: list[float] = self.__get_tkinter_pointlist()
        self.itemId = self._tk_object.create_polygon(coords=tkinter_pointlist, fill=self._background_color, outline=self._outline_color) #type:ignore
    
    def __get_tkinter_pointlist(self)->list[float]:
        getx: Callable[[vector2d], float] = lambda vector: vector.x
        gety: Callable[[vector2d], float] = lambda vector: vector.y
        return [f(point) for point in self._pointlist for f in (getx, gety)]
