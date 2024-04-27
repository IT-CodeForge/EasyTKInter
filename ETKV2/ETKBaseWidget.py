from __future__ import annotations
from abc import abstractmethod
from enum import Enum, auto
from typing import Optional
from .vector2d import vector2d
from .ETKBaseObject import ETKBaseObject


class __VALIDATION_RETURN_TYPES(Enum):
    OK = auto()
    INVALID = auto()
    LOCKED = auto()


class ETKBaseWidget(ETKBaseObject):
    def __init__(self, pos: vector2d, size: vector2d) -> None:
        ETKBaseObject.__init__(self, pos, size)
        self._parent: Optional[ETKBaseWidget] = None
        self._enabled: bool = True

    @property
    def parent(self) -> Optional[ETKBaseWidget]:
        return self._parent

    @ETKBaseObject.pos.setter
    def pos(self, value: vector2d):
        if self.parent != None:
            match self.parent.__validate_pos(value):
                case __VALIDATION_RETURN_TYPES.INVALID:
                    raise ValueError("invalid pos")
                case __VALIDATION_RETURN_TYPES.LOCKED:
                    raise RuntimeError(f"{self} is locked")
                case _:
                    pass
        self._pos = value

    @ETKBaseObject.size.setter
    def size(self, value: vector2d):
        if self.parent != None:
            match self.parent.__validate_size(value):
                case __VALIDATION_RETURN_TYPES.INVALID:
                    raise ValueError("invalid size")
                case __VALIDATION_RETURN_TYPES.LOCKED:
                    raise RuntimeError(f"{self} is locked")
                case _:
                    pass
        self._size = value

    @property
    def abs_pos(self) -> vector2d:
        """READ-ONLY"""
        if self._parent != None:
            return self._parent._get_childs_abs_pos(self)
        return self._pos

    @ETKBaseObject.visibility.setter
    def visibility(self, value: bool) -> None:
        self._visibility = value
        self._update_visibility()

    @property
    def enabled(self) -> bool:
        """READ-ONLY"""
        return self._enabled

    @property
    def abs_visibility(self) -> bool:
        """READ-ONLY"""
        if self._parent != None:
            return self._visibility and self._parent.abs_visibility
        return self._visibility

    @property
    def abs_enabled(self) -> bool:
        """READ-ONLY"""
        if self._parent != None:
            return self._enabled and self._parent._enabled
        return self._enabled

    def detach_child(self, element: ETKBaseWidget):
        if element._parent != self:
            raise ValueError(f"{self} is not the parent of {element}!")
        element._parent = None

    def detach_self(self):
        if self._parent == None:
            raise ValueError(f"{self} has no parent!")
        self._parent.detach_child(self)
    
    @abstractmethod
    def _update_pos(self) -> None:
        pass
    
    @abstractmethod
    def _update_visibility(self) -> None:
        pass

    def _update_enabled(self) -> None:
        pass

    def _get_childs_abs_pos(self, child: ETKBaseWidget) -> vector2d:
        return self.abs_pos + child.pos

    def __validate_pos(self, value: vector2d) -> __VALIDATION_RETURN_TYPES:
        return __VALIDATION_RETURN_TYPES.OK

    def __validate_size(self, value: vector2d) -> __VALIDATION_RETURN_TYPES:
        return __VALIDATION_RETURN_TYPES.OK
