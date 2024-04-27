from abc import abstractmethod
from tkinter import Event, Tk
from typing import Optional

from ETK.ETKCanvas import ETKCanvas # NOTE auf neuer Canvas
from .ETKUtils import gen_col_from_int
from .vector2d import vector2d
from .ETKBaseTkObject import ETKBaseTkObject
from .ETKBaseObject import Events


class WindowEvents(Events):
    MOUSE_MOVED = "<Motion>"
    KEY_PRESSED = "<KeyDown>"
    KEY_RELEASED = "<KeyRelease>"


class ETKMainWindow(ETKBaseTkObject):
    def __init__(self, pos: vector2d = vector2d(0, 0), size: vector2d = vector2d(2048, 512), caption: str = "Tk", background_color: int = 0xAAAAAA) -> None:
        self._tk_object: Tk = Tk()
        self.caption = caption
        self._pos = pos
        self._size = size
        self._topmost = False
        self.canvas = ETKCanvas(self._tk_object, 0, 0,
                                int(self.size.x), int(self.size.y))
        ETKBaseTkObject.__init__(self, pos, size, background_color)
        self._tk_object.protocol("WM_DELETE_WINDOW", self.app_close)
        self._event_lib.update({e: [] for e in WindowEvents})
        self._add_elements()

    @property
    def caption(self) -> str:
        return self._tk_object.title()

    @caption.setter
    def caption(self, value: str):
        self._tk_object.title(value)

    @ETKBaseTkObject.pos.setter
    def pos(self, value: vector2d):
        self._pos = value
        self.__place_object()

    @ETKBaseTkObject.size.setter
    def size(self, value: vector2d):
        self._size = value
        self.__place_object()

    @ETKBaseTkObject.background_color.setter
    def background_color(self, value: Optional[int]) -> None:
        ETKBaseTkObject.background_color.fset(self, value)  # type:ignore
        self._background_color = gen_col_from_int(value)
        self._tk_object.configure(background=self._background_color)
        self.canvas.object_id.configure(
            background=self._background_color)

    @ETKBaseTkObject.visibility.setter
    def visibility(self, value: bool) -> None:
        self._visibility = value
        if not value:
            self._tk_object.withdraw()
        else:
            self._tk_object.deiconify()
            self.force_focus()

    @property
    def topmost(self) -> bool:
        return self._topmost

    @topmost.setter
    def topmost(self, value: bool):
        self._topmost = value
        self._tk_object.attributes('-topmost', self._topmost)  # type:ignore

    def __place_object(self) -> None:
        self._tk_object.geometry(
            f"{self.size.x}x{self.size.y}+{self.pos.x}+{self.pos.y}")

    @abstractmethod
    def _add_elements(self) -> None:
        pass

    def app_close(self) -> None:
        exit()

    def run(self) -> None:
        self._tk_object.mainloop()

    def _handle_tk_event(self, event: Event) -> None:  # type:ignore
        match self._TK_EVENTTYPE_TRANSLATION[event.type]:
            case "<Motion>":
                self._handle_event(WindowEvents.MOUSE_MOVED,
                                   event)  # type:ignore
                return
            case "<KeyDown>":
                self._handle_event(WindowEvents.KEY_PRESSED,
                                   event)  # type:ignore
                return
            case "<KeyRelease>":
                self._handle_event(WindowEvents.KEY_RELEASED,
                                   event)  # type:ignore
                return
            case _:
                pass
        ETKBaseTkObject._handle_tk_event(self, event)  # type:ignore

    def force_focus(self) -> None:
        self._tk_object.attributes('-topmost', 1)  # type:ignore
        self._tk_object.focus_force()
        self._tk_object.attributes('-topmost', self._topmost)  # type:ignore
