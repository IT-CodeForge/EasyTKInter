from abc import abstractmethod
from typing import Any, Callable
from vector2d  import vector2d
from TGBaseObject import TGBaseObject
from enum      import Enum
from tkinter   import Event, Button
import logging

#this is for logging purposses, if you don't want it, set "log" to False
LOG = True
if LOG:
    my_logger = logging.getLogger("BaseWidget_logger")
    my_logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler = logging.FileHandler('project.log',mode='w')
    handler.setLevel(logging.DEBUG)
    handler.setFormatter(formatter)
    my_logger.addHandler(handler)
#-------------------------------------------------------------------------

class TGBaseWidget(TGBaseObject):
    def __init__(self, pos:vector2d, dim:vector2d) -> None:
        self.object_id: Any
        self.__visibility = True
        self.__object_pos = pos
        self.__dimensions = dim
        self.__place_object(self.__object_pos, self.__dimensions)
        super().__init__()
    
    @property
    def pos(self)->vector2d:
        return self.__object_pos
    
    @pos.setter
    def pos(self, value:vector2d):
        self.__place_object(value)
    
    @property
    def width(self)->int:
        return int(self.__dimensions.x)
    
    @width.setter
    def width(self, value:int):
        self.__dimensions.x = value
        self.__place_object()
    
    @property
    def height(self)->int:
        return int(self.__dimensions.y)
    
    @height.setter
    def height(self, value:int):
        self.__dimensions.y = value
        self.__place_object()
    
    @property
    def visible(self)->bool:
        return self.__visibility
    
    @visible.setter
    def visible(self, value:bool):
        if value:
            self.__visibility = True
            self.object_id.place()
        else:
            self.__visibility = False
            self.object_id.place_forget()
    
    def dissable(self):
        self.object_id["state"] = "disabled"
    
    def enable(self):
        self.object_id["state"] = "normal"

    def move(self, mov_vec:vector2d):
        self.pos = self.__object_pos+mov_vec

    def __place_object(self, pos:vector2d|None=None, dim:vector2d|None=None):
        if pos == None:
            pos = self.__object_pos
        else:
            self.__object_pos = pos
        if dim == None:
            dim = self.__dimensions
        else:
            self.__dimensions = dim
        self.object_id.place(x=pos.x, y=pos.y, width=dim.x, height=dim.y)