from __future__ import annotations
from tkinter import Event, Tk, EventType
from typing import Any

from .Internal.ETKBaseObject import ETKEvents
from .Vector2d import Vector2d
from .ETKLabel import ETKLabel
from .Internal.ETKBaseTkWidgetDisableable import ETKBaseTkWidgetDisableable


class ETKEditEvents(ETKEvents):
    CHANGED: ETKEditEvents
    CHANGED_DELAYED: ETKEditEvents
    _values = {"CHANGED": "<KeyRelease>", "CHANGED_DELAYED": "<KeyRelease>"}


class ETKEdit(ETKBaseTkWidgetDisableable, ETKLabel):
    def __init__(self, tk: Tk, pos: Vector2d = Vector2d(0, 0), size: Vector2d = Vector2d(80, 17), text: str = "Edit", *, visibility: bool = True, enabled: bool = True, background_color: int = 0xEEEEEE, text_color: int = 0, outline_color: int = 0x0, outline_thickness: int = 0, **kwargs: Any) -> None:
        self.__old_text: str = ""
        self.__delay_cycles: int = -1

        super().__init__(tk=tk, pos=pos, size=size, text=text, visibility=visibility, enabled=enabled,
                         background_color=background_color, text_color=text_color, outline_color=outline_color, outline_thickness=outline_thickness, **kwargs)

        self._tk_object["state"] = "normal"
        self._event_lib.update({e: [] for e in ETKEditEvents if e not in self._event_lib.keys()})

    # region Properties

    @ETKBaseTkWidgetDisableable.enabled.setter
    def enabled(self, value: bool) -> None:
        ETKBaseTkWidgetDisableable.enabled.fset(self, value)  # type:ignore
        if value:
            self._send_button_event_break = False
            self._tk_object.configure(cursor="xterm")
        else:
            self._send_button_event_break = True
            self._tk_object.configure(cursor="")

    @ETKLabel.text.setter
    def text(self, value: str) -> None:
        ETKLabel.text.fset(self, value)  # type:ignore
        self.__old_text = value

    # endregion
    # region Methods

    def __send_delayed_changed_event(self, event: Event) -> None:  # type:ignore
        if self.__delay_cycles == 0:
            self._handle_event(ETKEditEvents.CHANGED_DELAYED,
                               [event])  # type:ignore
        self.__delay_cycles -= 1

    def _handle_tk_event(self, event: Event) -> None | str:  # type:ignore
        match event.type:
            case EventType.KeyRelease:
                if self.abs_enabled and self.text != self.__old_text:
                    self.__delay_cycles += 1
                    self._handle_event(ETKEditEvents.CHANGED,
                                       [event])  # type:ignore
                    self._tk_object.after(1000, self.__send_delayed_changed_event, event)  # type:ignore
                    self.__old_text = self.text
                return
            case _:
                pass
        return super()._handle_tk_event(event)  # type:ignore

    # endregion
