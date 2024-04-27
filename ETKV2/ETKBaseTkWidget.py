from tkinter import Widget as tk_widget

from .vector2d import vector2d
from .ETKBaseWidget import ETKBaseWidget
from .ETKBaseTkObject import ETKBaseTkObject

class ETKBaseTkWidget(ETKBaseTkObject, ETKBaseWidget):
    
    def __init__(self, pos: vector2d, size: vector2d, background_color: int = 0xAAAAAA) -> None:
        self._tk_object: tk_widget
        ETKBaseWidget.__init__(self, pos, size)
        ETKBaseTkObject.__init__(self, pos, size, background_color)
        self.__place_object()

    @ETKBaseWidget.pos.setter
    def pos(self, value: vector2d):
        ETKBaseWidget.pos.fset(self, value) #type:ignore
        self._update_pos()
    
    @ETKBaseWidget.size.setter
    def size(self, value: vector2d):
        ETKBaseWidget.size.fset(self, value) #type:ignore
        self.__place_object()
    
    def _update_visibility(self) -> None:
        if self.abs_visibility:
            self.__place_object()
        else:
            self._tk_object.place_forget()
    
    def _update_pos(self) -> None:
        self.__place_object()
    
    def __place_object(self):
        anchor = vector2d()
        if self._parent != None:
            anchor = self._parent.abs_pos
        self._tk_object.place(x=self._pos.x + anchor.x, y=self._pos.y + anchor.y, width=self._size.x, height=self._size.y)