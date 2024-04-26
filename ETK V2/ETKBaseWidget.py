from __future__ import annotations
from abc import abstractmethod
from typing import Optional
from .vector2d import vector2d
from .ETKBaseObject import ETKBaseObject

class ETKBaseWidget(ETKBaseObject):
    def __init__(self, pos: vector2d, size: vector2d) -> None:
        super().__init__(pos, size)
        self._parent: Optional[ETKBaseWidget] = None
        self._visibility: bool = True
        self._enabled: bool = True
    
    @property
    def parent(self) -> Optional[ETKBaseWidget]:
        return self._parent
    
    @property
    def _abs_pos(self) -> vector2d:
        """READ-ONLY"""
        if self._parent != None:
            return self._parent._abs_pos + self._pos
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

    def detach(self, element: ETKBaseWidget):
        if element._parent != self:
            raise ValueError(f"{self} is not the parent of {element}!")
        element._parent = None