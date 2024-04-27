from __future__ import annotations
from abc import abstractmethod
from enum import Enum
from typing import Any, Callable, Optional
from .vector2d import vector2d


class Events(Enum):
    pass


class BaseEvents(Events):
    MOUSE_DOWN = "<ButtonPress>"
    MOUSE_UP = "<ButtonRelease>"
    ENTER = "<Enter>"
    LEAVE = "<Leave>"


class ETKBaseObject:
    def __init__(self, pos: vector2d, size: vector2d) -> None:
        self._pos: vector2d = pos
        self._size: vector2d = size
        self._event_lib: dict[Events, list[Callable[..., Any]]] = {
            e: [] for e in BaseEvents}

    @property
    def pos(self) -> vector2d:
        return self._pos

    @pos.setter
    @abstractmethod
    def pos(self, value: vector2d) -> None:
        pass

    @property
    def abs_pos(self) -> vector2d:
        """READ-ONLY"""
        return self._pos

    @property
    def size(self) -> vector2d:
        return self._size

    @size.setter
    @abstractmethod
    def size(self, value: vector2d):
        pass

    @property
    def events(self) -> dict[Events, list[Callable[..., Any]]]:
        """read-only"""
        return self._event_lib.copy()

    def add_event(self, event_type: Events, eventhandler: Callable[[], None] | Callable[[tuple[ETKBaseObject, Events, Any]], None]):
        self._event_lib[event_type].append(eventhandler)

    def remove_event(self, event_type: Events, eventhandler: Callable[[], None] | Callable[[tuple[ETKBaseObject, Events, Any]], None]):
        self._event_lib[event_type].remove(eventhandler)

    def _handle_event(self, event: Events, event_data: Optional[Any] = None):
        for c in self._event_lib[event]:
            try:
                c((self, event, event_data))
                continue
            except:
                pass
            try:
                c()
            except:
                ret_val = dict.get(  # type:ignore
                    "eventhandler").__code__.co_varnames
                name = dict.get("eventhandler").__name__  # type:ignore
                raise TypeError(
                    f"Invalid parametercount for event function ({name}) (can only be 0,1 or 3 self is not included),parameters: {ret_val}")  # NOTE
