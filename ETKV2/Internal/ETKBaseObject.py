from __future__ import annotations
from abc import abstractmethod
from enum import Enum, auto
from typing import Any, Callable, Optional
from ..vector2d import vector2d


class Events(Enum):
    pass


class BaseEvents(Events):
    MOUSE_DOWN = ("<ButtonPress>", auto())
    MOUSE_UP = ("<ButtonRelease>", auto())
    ENTER = ("<Enter>", auto())
    LEAVE = ("<Leave>", auto())
    MOUSE_MOVED = ("<Motion>", auto())


class ETKBaseObject:
    def __init__(self, pos: vector2d, size: vector2d) -> None:
        self._pos: vector2d = vector2d()
        self._size: vector2d = vector2d()
        self.pos = pos
        self.size = size
        self._visibility: bool = True
        self._event_lib: dict[Events, list[Callable[..., Any]]] = {
            e: [] for e in BaseEvents}

    # region Properties

    @property
    def pos(self) -> vector2d:
        return self._pos.copy()

    @pos.setter
    @abstractmethod
    def pos(self, value: vector2d) -> None:
        pass

    @property
    def abs_pos(self) -> vector2d:
        """READ-ONLY"""
        return self._pos.copy()

    @property
    def size(self) -> vector2d:
        return self._size.copy()

    @size.setter
    @abstractmethod
    def size(self, value: vector2d) -> None:
        pass

    @property
    def visibility(self) -> bool:
        return self._visibility

    @visibility.setter
    @abstractmethod
    def visibility(self, value: bool) -> None:
        pass

    @property
    def abs_visibility(self) -> bool:
        """READ-ONLY"""
        return self._visibility

    @property
    def events(self) -> dict[Events, list[Callable[..., Any]]]:
        """READ-ONLY"""
        return self._event_lib.copy()

    # endregion
    #region Methods
    #region Eventhandling Methods

    def add_event(self, event_type: Events, eventhandler: Callable[[], None] | Callable[[tuple[ETKBaseObject, Events, Any]], None]) -> None:
        self._event_lib[event_type].append(eventhandler)

    def remove_event(self, event_type: Events, eventhandler: Callable[[], None] | Callable[[tuple[ETKBaseObject, Events, Any]], None]) -> None:
        self._event_lib[event_type].remove(eventhandler)

    def _handle_event(self, event: Events, event_data: Optional[Any] = None) -> None:
        for c in self._event_lib[event]:
            try:
                c((self, event, event_data))
                continue
            except:
                pass
            try:
                c()
            except:
                ret_val = c.__code__.co_varnames
                name = c.__name__  # type:ignore
                raise TypeError(
                    f"invalid parametercount for event function ({name}) (can only be 0, 1 (self, cls, etc not included)), parameter: {ret_val}")
    
    #endregion
    #endregion
