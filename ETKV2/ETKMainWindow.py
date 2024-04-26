from abc import abstractmethod
from tkinter import Tk
from typing import Optional

from ETK.ETKCanvas import ETKCanvas
from .ETKUtils import gen_col_from_int
from .vector2d import vector2d
from .ETKBaseTkObject import ETKBaseTkObject

class ETKMainWindow(ETKBaseTkObject):
    def __init__(self, pos: vector2d = vector2d(0, 0), size: vector2d = vector2d(2048, 512), caption: str = "Tk", background_color: int = 0xAAAAAA) -> None:
        self._tk_object: Tk = Tk()
        self.caption = caption
        self._pos = pos
        self._size = size
        self.canvas = ETKCanvas(self._tk_object, 0, 0, int(self.size.x), int(self.size.y))
        super().__init__(pos, size, background_color)
        self.__place_object()
        self._tk_object.protocol("WM_DELETE_WINDOW", self.app_close)

        #TODO: EVENTS

        self.add_elements()


    @property
    def caption(self) -> str:
        return self._tk_object.title()

    @caption.setter
    def caption(self, value: str):
        self._tk_object.title(value)

    @ETKBaseTkObject.pos.setter
    def pos(self, value: vector2d):#
        self._pos = value
        self.__place_object()
    
    @ETKBaseTkObject.size.setter
    def size(self, value: vector2d):
        self._size = value
        self.__place_object()

    @ETKBaseTkObject.background_color.setter
    def background_color(self, value: Optional[int]) -> None:
        ETKBaseTkObject.background_color.fset(self, value) #type:ignore #NOTE
        self._background_color = gen_col_from_int(value)
        self._tk_object.configure(background=self._background_color)
        self.canvas.object_id.configure(background=self._background_color) #NOTE
    
    def __place_object(self) -> None:
        self._tk_object.geometry(f"{self.size.x}x{self.size.y}+{self.pos.x}+{self.pos.y}")

    @abstractmethod
    def add_elements(self):
        pass

    def app_close(self) -> None:
        #TODO: CLOSE_EVENT
        exit()
    
    def run(self) -> None:
        self._tk_object.mainloop()