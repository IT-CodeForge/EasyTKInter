from tkinter import Event, EventType
from typing import Any, Callable, Optional

from ..vector2d import vector2d
from .ETKBaseObject import ETKBaseObject, Events, BaseEvents
from .ETKUtils import gen_col_from_int


class ETKBaseTkObject(ETKBaseObject):
    def __init__(self, pos: vector2d, size: vector2d, background_color: int = 0xAAAAAA) -> None:
        ETKBaseObject.__init__(self, pos, size)
        self._tk_object: Any
        self._background_color = ""
        self.background_color = background_color

    # region Properties

    @property
    def background_color(self) -> int:
        return int(self._background_color[1:], 16)

    @background_color.setter
    def background_color(self, value: Optional[int]) -> None:
        self._background_color = gen_col_from_int(value)
        self._tk_object.configure(background=self._background_color)

    # endregion
    # region Methods
    # region Eventhandling Methods

    def add_event(self, event_type: Events, eventhandler: Callable[[], None] | Callable[[tuple[ETKBaseObject, Events, Any]], None]) -> None:
        if event_type.value[0] != "<Custom>":
            if len(self._event_lib[event_type]) == 0:
                self._tk_object.bind(
                    event_type.value[0], self._handle_tk_event)  # type:ignore
        ETKBaseObject.add_event(self, event_type, eventhandler)

    def remove_event(self, event_type: Events, eventhandler: Callable[[], None] | Callable[[tuple[ETKBaseObject, Events, Any]], None]) -> None:
        if event_type.value[0] != "<Custom>":
            if len(self._event_lib[event_type]) == 0:
                self._tk_object.unbind(event_type.value[0])
        ETKBaseObject.remove_event(self, event_type, eventhandler)

    def _handle_tk_event(self, event: Event, event_object: Optional[ETKBaseObject] = None) -> None:  # type:ignore
        match event.type:
            case EventType.ButtonPress:
                event_type = BaseEvents.MOUSE_DOWN
            case EventType.ButtonRelease:
                event_type = BaseEvents.MOUSE_UP
            case EventType.Enter:
                event_type = BaseEvents.ENTER
            case EventType.Leave:
                event_type = BaseEvents.LEAVE
            case EventType.Motion:
                event_type = BaseEvents.MOUSE_MOVED
            case _:
                raise ValueError(f"invalid event {event}")

        self._handle_event(event_type, event, event_object)  # type:ignore

    # endregion
    # endregion
