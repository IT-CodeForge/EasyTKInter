from enum import auto
from tkinter import Event, Tk, EventType
from typing import Optional

from .Internal.ETKBaseObject import ETKBaseObject
from .Internal.ETKBaseObject import Events
from .vector2d import vector2d
from .ETKLabel import ETKLabel
from .Internal.ETKBaseTkWidgetDisableable import ETKBaseTkWidgetDisableable


class EditEvents(Events):
    CHANGED = ("<KeyPress>", auto())


class ETKEdit(ETKBaseTkWidgetDisableable, ETKLabel):
    def __init__(self, tk: Tk, text: str, pos: vector2d = vector2d(0, 0), size: vector2d = vector2d(80, 17), background_color: int = 11184810, text_color: int = 0) -> None:
        ETKLabel.__init__(self, tk, text, pos, size,
                          background_color, text_color)
        self._tk_object["state"] = "normal"
        ETKBaseTkWidgetDisableable.__init__(self, pos, size, background_color)
        self._event_lib.update({e: [] for e in EditEvents})

    # region Methods

    def _handle_tk_event(self, event: Event, event_object: Optional[ETKBaseObject] = None) -> None: # type:ignore
        match event.type:
            case EventType.KeyPress:
                if self._enabled:
                    self._handle_event(EditEvents.CHANGED,
                                       event, event_object)  # type:ignore
                    return
            case _:
                pass
        ETKBaseTkWidgetDisableable._handle_tk_event(  # type:ignore
            self, event, event_object)

    # endregion
