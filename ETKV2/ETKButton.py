from .ETKBaseObject import Events
from .ETKBaseTkWidgetDisableable import ETKBaseTkWidgetDisableable
from .ETKBaseTkWidgetText import ETKBaseTkWidgetText
from .vector2d import vector2d
from tkinter import Button, Event, Tk, EventType


class ButtonEvents(Events):
    BUTTON_PRESSED = "<ButtonPress>"
    BUTTON_RELEASED = "<ButtonRelease>"


class ETKButton(ETKBaseTkWidgetDisableable, ETKBaseTkWidgetText):
    def __init__(self, tk: Tk, text: str = "", pos: vector2d = vector2d(0, 0), size: vector2d = vector2d(70, 18), background_color: int = 0xEEEEEE, text_color: int = 0x0) -> None:
        self._tk_object: Button = Button(tk)  # type:ignore
        ETKBaseTkWidgetDisableable.__init__(self, pos, size, background_color)
        ETKBaseTkWidgetText.__init__(
            self, text, pos, size, background_color, text_color)
        self._event_lib.update({e: [] for e in ButtonEvents})

    def _handle_tk_event(self, event: Event) -> None:  # type:ignore
        match event.type:
            case EventType.ButtonPress:
                if self._enabled:
                    self._handle_event(
                        ButtonEvents.BUTTON_PRESSED, event)  # type:ignore
            case EventType.ButtonRelease:
                if self._enabled:
                    self._handle_event(
                        ButtonEvents.BUTTON_RELEASED, event)  # type:ignore
            case _:
                pass
        return ETKBaseTkWidgetText._handle_tk_event(self, event)  # type:ignore
