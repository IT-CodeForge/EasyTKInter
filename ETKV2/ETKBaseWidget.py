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
        self._visibility: bool = True
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
            return self._parent.abs_pos + self._pos
        return self._pos

    @property
    def visibility(self) -> bool:
        return self._visibility
    
    @visibility.setter
    @abstractmethod
    def visibility(self, value: bool) -> None:
        pass

    @property
    def enabled(self) -> bool:
        """READ-ONLY""" #NOTE
        return self._enabled
    
    @property
    def _abs_visibility(self) -> bool:
        """READ-ONLY"""
        if self._parent != None:
            return self._visibility and self._parent._abs_visibility
        return self._visibility
    
    @property
    def _abs_enabled(self) -> bool:
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
    
    def __validate_pos(self, value: vector2d) -> __VALIDATION_RETURN_TYPES:
        return __VALIDATION_RETURN_TYPES.OK

    def __validate_size(self, value: vector2d) -> __VALIDATION_RETURN_TYPES:
        return __VALIDATION_RETURN_TYPES.OK