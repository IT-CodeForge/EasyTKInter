from typing import Any, Callable
from vector2d  import vector2d
from TGBaseObject import TGBaseObject
from enum      import Enum
from tkinter   import Event
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


class BaseEvents(Enum):
    EV_MOUSE_DOWN   = 0
    EV_MOUSE_UP     = 1
    EV_HOVERED      = 2
    EV_STOP_HOVERED = 3

class TGBaseWidget(TGBaseObject):
    def __init__(self, pos:vector2d, dim:vector2d) -> None:
        self.object_id: Any
        self.__object_pos = pos
        self.__dimensions = dim
        self.__place_object(self.__object_pos, self.__dimensions)
        self.__event_funcs:dict[BaseEvents,Callable[...,None]] = {}
        self.__event_trans:dict[BaseEvents, list[str|Callable[...,None]]] = {
                            BaseEvents.EV_MOUSE_DOWN:["<ButtonPress>", self.__ev_mouse_down, ""],
                            BaseEvents.EV_MOUSE_UP:["<ButtonRelease>", self.__ev_mouse_up, ""],
                            BaseEvents.EV_HOVERED:["<Enter>", self.__ev_mouse_hovered, ""],
                            BaseEvents.EV_STOP_HOVERED:["<Leave>", self.__ev_mouse_stop_hovered, ""]}
    
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
    
    def _handle_event(self, func:Callable[...,None], event_type:BaseEvents|Any, event:Event):
        if self.object_id["state"] == "disabled" and type(event_type) != BaseEvents:
            return
        super()._handle_event(func,{"object_id":self.object_id,"event_type":event_type,"event":event,"mousepos":vector2d(event.x,event.y)})

    def add_event(self, event_type:BaseEvents, eventhandler:Callable[...,None]):
        self.__event_funcs[event_type] = eventhandler
        self.__event_trans[event_type][2] = self.object_id.bind(self.__event_trans[event_type][0], self.__event_trans[event_type][1])

    def remove_event(self, event_type:BaseEvents):
        self.object_id.unbind(event_type, funcid=self.__event_trans[event_type][2])
        self.__event_funcs.pop(event_type)

    def __ev_mouse_down(self, event:Event):
        self._handle_event(self.__event_funcs[BaseEvents.EV_MOUSE_DOWN], BaseEvents.EV_MOUSE_DOWN, event)

    def __ev_mouse_up(self, event:Event):
        self._handle_event(self.__event_funcs[BaseEvents.EV_MOUSE_UP], BaseEvents.EV_MOUSE_UP, event)

    def __ev_mouse_hovered(self, event:Event):
        self._handle_event(self.__event_funcs[BaseEvents.EV_HOVERED], BaseEvents.EV_HOVERED, event)
    
    def __ev_mouse_stop_hovered(self, event:Event):
        self._handle_event(self.__event_funcs[BaseEvents.EV_STOP_HOVERED], BaseEvents.EV_STOP_HOVERED, event)