from abc import abstractmethod
from tkinter import Tk

from ETK.ETKCanvas import ETKCanvas
from .vector2d import vector2d
from .ETKBaseTkObject import ETKBaseTkObject

class ETKMainWindow(ETKBaseTkObject):
    def __init__(self, pos: vector2d = vector2d(0, 0), size: vector2d = vector2d(2048, 512), caption: str = "Tk", background_color: int = 0xAAAAAA) -> None:
        self._tk_object: Tk = Tk()
        super().__init__(pos, size, background_color)
        self.caption = caption
        self._pos = pos
        self._size = size
        self.__place_object()
        self._tk_object.protocol("WM_DELETE_WINDOW", self.app_close)
        self.canvas = ETKCanvas(self._tk_object, 0, 0, int(self.size.x), int(self.size.y))

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
    
    def __place_object(self) -> None:
        self._tk_object.geometry(f"{self.size.x}x{self.size.y}+{self.pos.x}+{self.pos.y}")

    @abstractmethod
    def add_elements(self):
        pass

    def app_close(self) -> None:
        #TODO: CLOSE_EVENT
        exit()