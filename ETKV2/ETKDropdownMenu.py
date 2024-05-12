from typing import Any
from .vector2d import vector2d
from .Internal.ETKBaseTkWidgetDisableable import ETKBaseTkWidgetDisableable
from .Internal.ETKBaseObject import ETKEvents
from enum import auto
from tkinter import OptionMenu, StringVar, Tk


class ETKDropdownMenuEvents(ETKEvents):
    CHANGED = ("<Custom>", auto())


class ETKDropdownMenu(ETKBaseTkWidgetDisableable):
    def __init__(self, tk: Tk, options: list[str], start_value: str = "", pos: vector2d = vector2d(0, 0), size: vector2d = vector2d(70, 18), background_color: int = 0xEEEEEE, **kwargs: Any) -> None:
        self.__selected = StringVar(value=start_value)
        self._tk_object = OptionMenu(tk, self.__selected, *options)
        self.__ignore_next_change_event = False

        super().__init__(pos=pos, size=size, background_color=background_color, **kwargs)

        self.__selected.trace("w", self.__clicked_changed)  # type:ignore
        self._event_lib.update({e: [] for e in ETKDropdownMenuEvents})

    @property
    def selected(self) -> str:
        return self.__selected.get()
    
    @selected.setter
    def selected(self, value: str) -> None:
        self.__ignore_next_change_event = True
        self.__selected.set(value)

    def __clicked_changed(self, *args: str) -> None:
        if not self.__ignore_next_change_event:
            self._handle_event(ETKDropdownMenuEvents.CHANGED)
        else:
            self.__ignore_next_change_event = False

