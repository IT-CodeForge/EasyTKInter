from typing import Any
from .vector2d  import vector2d
from .ETKBaseObject import ETKBaseObject
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

class ETKBaseWidget(ETKBaseObject):
    def __init__(self, pos:vector2d, dim:vector2d) -> None:
        super().__init__()
        self.object_id: Any
        self.__visibility = True
        self.__object_pos = pos
        self.__dimensions = dim
        self.__place_object(self.__object_pos, self.__dimensions)
        self.__state = True

    @property
    def abs_pos(self)->vector2d:
        """
        READ-ONLY \r\n
        the absolute position in the Window
        """
        return self.__object_pos + vector2d() if self.parent == 0 else self._parent.abs_pos

    @property
    def pos(self)->vector2d:
        """
        The position relative to the parent (eg. if object, is added to Container, the Container becomes its parent)\r\n
        WARNING: Some Parents may lock the position and make it READ-ONLY
        """
        return self.__object_pos
    
    @pos.setter
    def pos(self, value:vector2d):
        if self.parent != None and not self._parent._validate("move", self):
            print("WARNING: tried to move a locked Element")
            return
        self.__place_object(value)
        if self.parent != None and self._parent._validate("move", self):
            self._parent._element_changed(self)
    
    @property
    def width(self)->int:
        """
        The width of the element
        """
        return int(self.__dimensions.x)
    
    @width.setter
    def width(self, value:int):
        if self.parent != None and not self._parent._validate("width", self):
            return
        self.__dimensions.x = value
        self.__place_object()
        if self.parent != None and self._parent._validate("width", self):
            self._parent._element_changed(self)
    
    @property
    def height(self)->int:
        """
        the height of the element
        """
        return int(self.__dimensions.y)
    
    @height.setter
    def height(self, value:int):
        if self.parent != None and not self._parent._validate("height", self):
            return
        self.__dimensions.y = value
        self.__place_object()
        if self.parent != None and self._parent._validate("height", self):
            self._parent._element_changed(self)
    
    @property
    def visible(self)->bool:
        """
        If the element, is drawn on the window\r\n
        WARNING: When parents are set invisible the children are never drawn, but they remember their status and their status can still be changed, so upon making the parent visible again, only the children which,
        before or during the the parent being invisible were set to visible will be drawn
        """
        return self.__visibility
    
    @visible.setter
    def visible(self, value:bool):
        if value:
            self.__visibility = True
            if self.parent != None and not self._parent._validate("visible", self):
                return
            self.__place_object()
            self._eventhandler("<Visible>")
        else:
            self.__visibility = False
            if self.parent != None and not self._parent._validate("visible", self):
                return
            self.object_id.place_forget()
            self._eventhandler("<Visible>")
        if self.parent != None and self._parent._validate("visible", self):
            self._parent._element_changed(self)
    
    @property
    def enabled(self)->bool:
        """
        Defines, if the element, can be interacted with, by the user
        """
        return self.__state
    
    @enabled.setter
    def enabled(self, value):
        self.__state = value
        if self.__state:
            self.object_id["state"] = "normal"
        else:
            self.object_id["state"] = "disabled"

    def move(self, mov_vec:vector2d):
        """
        moves an element from its current position, by the mov_vec
        """
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
        anchor = vector2d()
        if self.parent != None:
            anchor = self._parent.abs_pos
        self.object_id.place(x=pos.x + anchor.x, y=pos.y + anchor.y, width=dim.x, height=dim.y)
    
    def detach(self):
        """
        detaches the object, from its parent
        """
        self._eventhandler("<Detach>")