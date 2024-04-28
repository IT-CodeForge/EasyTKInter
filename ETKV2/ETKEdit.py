from enum import auto
from tkinter import Event, Tk, EventType

from .Internal.ETKBaseObject import Events
from .vector2d import vector2d
from .ETKLabel import ETKLabel
from .Internal.ETKBaseTkWidgetDisableable import ETKBaseTkWidgetDisableable
from .Internal.ETKBaseTkObject import BaseEvents  # type:ignore


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

    def _handle_tk_event(self, event: Event) -> None:  # type:ignore
        match event.type:
            case EventType.KeyPress:
                if self._enabled:
                    self._handle_event(EditEvents.CHANGED,
                                       [event])  # type:ignore
                    return
            case _:
                pass
        ETKBaseTkWidgetDisableable._handle_tk_event(  # type:ignore
            self, event)

    # endregion
