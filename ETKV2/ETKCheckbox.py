from enum import auto
from typing import Optional

from .Internal.ETKBaseObject import ETKBaseObject
from .vector2d import vector2d
from .Internal.ETKBaseObject import Events
from .Internal.ETKBaseTkWidgetDisableable import ETKBaseTkWidgetDisableable
from .Internal.ETKBaseTkWidgetText import ETKBaseTkWidgetText
from tkinter import Checkbutton, IntVar, Event, Tk, EventType


class CheckboxEvents(Events):
    CHECKED = ("<ButtonPress>", auto())
    UNCHECKED = ("<ButtonPress>", auto())
    TOGGLED = ("<ButtonPress>", auto())


class ETKCheckbox(ETKBaseTkWidgetDisableable, ETKBaseTkWidgetText):
    def __init__(self, tk: Tk, text: str = "", pos: vector2d = vector2d(0, 0), size: vector2d = vector2d(70, 18), background_color: int = 0xEEEEEE, text_color: int = 0x0) -> None:
        self.__state = IntVar()
        self._tk_object: Checkbutton = Checkbutton(  # type:ignore
            tk, variable=self.__state)
        ETKBaseTkWidgetDisableable.__init__(self, pos, size, background_color)
        ETKBaseTkWidgetText.__init__(
            self, text, pos, size, background_color, text_color)
        self._event_lib.update({e: [] for e in CheckboxEvents})

    # region Properties

    @property
    def state(self) -> bool:
        return bool(self.__state.get())

    @state.setter
    def state(self, value: bool) -> None:
        self.__state.set(value)

    # endregion
    # region Methods

    def _handle_tk_event(self, event: Event, event_object: Optional[ETKBaseObject] = None) -> None:  # type:ignore
        match event.type:
            case EventType.ButtonPress:
                if self.enabled:
                    self._handle_event(
                        CheckboxEvents.TOGGLED, event, event_object)  # type:ignore
                    if self.state:
                        self._handle_event(
                            CheckboxEvents.CHECKED, event, event_object)  # type:ignore
                    else:
                        self._handle_event(
                            CheckboxEvents.UNCHECKED, event, event_object)  # type:ignore
            case _:
                pass
        ETKBaseTkWidgetText._handle_tk_event(self, event, event_object)  # type:ignore

    # endregion
