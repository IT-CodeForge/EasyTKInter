from tkinter import Event, Tk
from .ETKBaseObject import Events
from .vector2d import vector2d
from .ETKLabel import ETKLabel
from .ETKBaseTkWidgetDisableable import ETKBaseTkWidgetDisableable

class EditEvents(Events):
    EV_CHANGED = "<KeyPress>"

class ETKEdit(ETKBaseTkWidgetDisableable, ETKLabel):
    def __init__(self, myTk:Tk, text: str, pos: vector2d = vector2d(0, 0), size: vector2d = vector2d(80, 17), background_color: int = 11184810, text_color: int = 0) -> None:
        ETKLabel.__init__(self, myTk, text, pos, size, background_color, text_color)
        self._tk_object["state"] = "normal"
        ETKBaseTkWidgetDisableable.__init__(self, pos, size, background_color)
        self._event_lib.update({e: [] for e in EditEvents})

    def _handle_tk_event(self, event: Event) -> None: #type:ignore
        match self._TK_EVENTTYPE_TRANSLATION[event.type]:
            case "<KeyPress>":
                if self._enabled:
                    self._handle_event(EditEvents.EV_CHANGED, event) #type:ignore
                    return
            case _:
                pass
        super()._handle_tk_event(event) #type:ignore