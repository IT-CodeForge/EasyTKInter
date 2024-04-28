from __future__ import annotations
from abc import abstractmethod
from typing import Optional
from ..vector2d import vector2d
from .ETKBaseObject import ETKBaseObject


class ETKBaseWidget(ETKBaseObject):
    def __init__(self, pos: vector2d, size: vector2d) -> None:
        self._parent: Optional[ETKBaseWidget] = None
        self._enabled: bool = True
        ETKBaseObject.__init__(self, pos, size)

    @property
    def parent(self) -> Optional[ETKBaseWidget]:
        return self._parent

    @ETKBaseObject.pos.setter
    def pos(self, value: vector2d) -> None:
        self._pos = value
        if self.parent != None:
            self.parent._validate_pos(self)
        self._update_pos()

    @ETKBaseObject.size.setter
    def size(self, value: vector2d) -> None:
        self._size = value
        if self.parent != None:
            self.parent._validate_size(self)

    @property
    def abs_pos(self) -> vector2d:
        """READ-ONLY"""
        if self._parent != None:
            return self._parent._get_childs_abs_pos(self)
        return self._pos.copy()

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

    def _detach_child(self, element: ETKBaseWidget) -> None:
        if element._parent != self:
            raise ValueError(f"{self} is not the parent of {element}!")
        element._parent = None

    def detach_from_parent(self) -> None:
        if self._parent == None:
            raise ValueError(f"{self} has no parent!")
        self._parent._detach_child(self)

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

    def _validate_pos(self, element: ETKBaseWidget) -> None:
        pass

    def _validate_size(self, element: ETKBaseWidget) -> None:
        pass
