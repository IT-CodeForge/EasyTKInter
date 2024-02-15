from typing import overload
from TGBaseObject import BaseEvents
from vector2d     import vector2d
from enum         import Enum

class Alignments(Enum):
    TOP_LEFT      = "00"
    TOP_CENTER    = "01"
    TOP_RIGHT     = "02"
    MIDDLE_LEFT   = "10"
    MIDDLE_CENTER = "11"
    MIDDLE_RIGHT  = "12"
    BOTTOM_LEFT   = "20"
    BOTTOM_CENTER = "21"
    BOTTOM_RIGHT  = "22"

class TGContainer:
    @overload
    def __init__(self, pos_x:int, pos_y:int, width:int, height:int) -> None:
        self.__my_pos = vector2d(pos_x, pos_y)
        self.__dimensions = vector2d(width, height)
        self.__anchor = vector2d()
        self.__elements = []
    
    def __init__(self, gui_object):
        self.__my_pos = gui_object.pos
        self.__dimensions = vector2d(gui_object.width, gui_object.height)
        self.__anchor = vector2d()
        self.__elements = []
    
    @property
    def anchor(self)->vector2d:
        return self.__anchor
    
    @anchor.setter
    def anchor(self, value:vector2d):
        self.__anchor = value
        self.__place_elements()

    @property
    def pos(self)->vector2d:
        return self.__my_pos
    
    @pos.setter
    def pos(self, value:vector2d):
        self.__my_pos = value
        self.__place_elements()
    
    @property
    def width(self)->int:
        return self.__dimensions.x
    
    @width.setter
    def width(self, value:int):
        self.__dimensions.x = value
        self.__place_elements()
    
    @property
    def height(self)->int:
        return self.__dimensions.y
    
    @height.setter
    def height(self, value:int):
        self.__dimensions.y = value
        self.__place_elements()
    
    def add_element(self, element, allignment:Alignments=Alignments.TOP_LEFT):
        self.__elements.append([element, vector2d(int(allignment.value[1]), int(allignment.value[0]))])
        self.__place_elements()
        element.add_event(BaseEvents.CONFIGURED, self.__ev_element_configured)
    
    def remove_element(self, element):
        element.remove_event(BaseEvents.CONFIGURED)
        for my_element in self.__elements:
            if my_element[0] == element:
                self.__elements.remove(my_element)
                self.__place_elements()
                break

    def __place_elements(self):
        for element in self.__elements:
            element[0].anchor = self.__my_pos + self.anchor
            element_pos = (self.__dimensions - vector2d(element[0].width, element[0].height)) * element[1] / 2
            element[0].pos = element_pos + element[0].pos
    
    def __ev_element_configured(self, params:dict):
        element = params.get("object_id")
        for my_element in self.__elements:
            if my_element[0].object_id == element:
                if my_element[0].anchor != self.__my_pos:
                    my_element[0].anchor = self.__my_pos