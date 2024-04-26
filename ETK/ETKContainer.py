from .ETKBaseWidget import ETKBaseWidget
from .ETKNoTKEventBase import ETKNoTKEventBase
from .ETKBaseObject import BaseEvents
from .vector2d     import vector2d
from enum         import Enum
import logging

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

class ETKContainer(ETKNoTKEventBase):
    def __init__(self, gui_object=None):
        super().__init__()
        self.__elements = []
        self.__visibility = True
        self.__mov_flag = False
        if gui_object == None:
            self.__my_pos = vector2d()
            self.__dimensions = vector2d()
            self.width = None
            self.height = None
        else:
            self.__my_pos = gui_object.pos
            self.__dimensions = vector2d(gui_object.width, gui_object.height)

    ######
    ###properties###
    ######    
    @property
    def abs_pos(self)->vector2d:
        """
        READ-ONLY \r\n
        the absolute position in the Window
        """
        return self.__my_pos + vector2d() if self.parent == None else self._parent.abs_pos

    @property
    def pos(self)->vector2d:
        """
        The position relative to the parent (eg. if object, is added to Container, the Container becomes its parent)\r\n
        WARNING: Some Parents may lock the position and make it READ-ONLY
        """
        return self.__my_pos
    
    @pos.setter
    def pos(self, value:vector2d):
        if self.parent != None and not self._parent._validate("move", self):
            return
        my_pos = self.__my_pos
        self.__my_pos = value
        if my_pos != value:
            self._eventhandler(BaseEvents.CONFIGURED)
        self.__place_elements()
        if self.parent != None and self._parent._validate("move", self):
            self._parent._element_changed(self)
    
    @property
    def width(self)->int:
        """
        The width of the element, if width is set to None, it becomes dynamic
        """
        if self.__dimensions.x == -1:
            return max([e[0].pos.x + e[0].width for e in self.__elements])
        return self.__dimensions.x
    
    @width.setter
    def width(self, value:int):
        if self.parent != None and not self._parent._validate("width",self):
            return
        if type(value) == int and value < 0:
            raise ValueError("objects must have a positive width")
        if value == None:
            value = -1
        my_width = self.__dimensions.x
        self.__dimensions.x = value
        if my_width != value:
            self._eventhandler(BaseEvents.CONFIGURED)
        self.__place_elements()
        if self.parent != None and self._parent._validate("width", self):
            self._parent._element_changed(self)
    
    @property
    def height(self)->int:
        """
        the height of the element, if height is set to None, it becomes dynamic
        """
        if self.__dimensions.y == -1:
            return max([e[0].pos.y + e[0].height for e in self.__elements])
        return self.__dimensions.y
    
    @height.setter
    def height(self, value:int):
        if self.parent != None and not self._parent._validate("height", self):
            return
        if type(value) == int and value < 0:
            raise ValueError("objects must have a positive height")
        if value == None:
            value = -1
        my_height = self.__dimensions.y
        self.__dimensions.y = value
        if my_height != value:
            self._eventhandler(BaseEvents.CONFIGURED)
        self.__place_elements()
        if self.parent != None and self._parent._validate("height", self):
            self._parent._element_changed(self)
    
    @property
    def visible(self)->bool:
        return self.__visibility
    
    @visible.setter
    def visible(self, value):
        """
        If the children, are drawn on the window\r\n
        WARNING: When parents are set invisible the children are never drawn, but they remember their status and their status can still be changed, so upon making the parent visible again, only the children which,
        before or during the the parent being invisible were set to visible will be drawn
        """
        if self.parent != None and not self._parent._validate("visible", self):
            self.__visibility = value
            return
        visibilities = []
        for e in self.__elements:
            visibilities.append(e[0].visible)
            e[0].visible = False
        self.__visibility = value
        for index,e in enumerate(self.__elements):
            e[0].visible = visibilities[index]
        self._eventhandler("<Visible>")
        if self.parent != None and self._parent._validate("visible", self):
            self._parent._element_changend(self)
    ######
    ######
    ######

    ######
    ###manipulating elements###
    ######
    def add_element(self, element, allignment:Alignments=Alignments.TOP_LEFT):
        self.__elements.append([element, vector2d(int(allignment.value[1]), int(allignment.value[0]))])
        self.__place_elements()
        element.add_event("<Detach>", self.__ev_element_detached, lambda event, object_id : True)
        element._parent = self
    
    def remove_element(self, element):
        for my_element in self.__elements:
            if my_element[0] == element:
                element.remove_event("<Detach>", self.__ev_element_detached, lambda event, object_id : True)
                element.pos -= self.pos
                element._parent = None
                self.__elements.remove(my_element)
                break   
    ######
    ######
    ######

    ######
    ###calculate child positions###
    ######
    def __place_elements(self):
        if len(self.__elements) == 0:
            return
        dynamic_dim = self.__get_dynamic_dim()
        for element in self.__elements:
            if element[0].pos.x + element[0].width > dynamic_dim.x or element[0].pos.y + element[0].height > dynamic_dim.y:
                continue 
            element_pos = (dynamic_dim - vector2d(element[0].width, element[0].height)) * element[1] / 2
            element[0].pos = element_pos + element[0].pos
    
    def __get_dynamic_dim(self)->vector2d:
        max_x = max([e[0].pos.x + e[0].width for e in self.__elements])
        max_y = max([e[0].pos.y + e[0].height for e in self.__elements])
        retval = vector2d(max_x if self.__dimensions.x == -1 else self.__dimensions.x,
                          max_y if self.__dimensions.y == -1 else self.__dimensions.y)
        return retval
    ######
    ######
    ######

    ######
    ###Events###
    ######    
    def __ev_element_detached(self, params):
        my_object = params.get("object_id")
        if type(my_object) == ETKBaseWidget:
            for element in self.__elements:
                if element.object_id == my_object:
                    my_object = element
                    break
        for my_element in self.__elements:
            if my_element[0] == element:
                self.__elements.remove(my_element)
                break
        my_object.pos = vector2d()
        my_object.visible = False
    
    def detach(self):
        """
        detaches the object, from its parent
        """
        self._eventhandler("<Detach>")  
    ######
    ######
    ######

    ######
    ###methods as parent###
    ######
    def _validate(self, action:str, child)->bool:
        if action == "move":    
            if self.__mov_flag:
                self.__mov_flag = False
                return False
            self.__mov_flag = True
            return False
        
        if action == "visible":
            return self.visible
        
        return True
    
    def _element_changed(self, child):
        self.__place_elements()

        if None == self.height and self.parent != None:
            self.parent._element_changed()
        
        if None == self.width and self.parent != None:
            self._parent._element_changed()
    ######
    ######
    ######