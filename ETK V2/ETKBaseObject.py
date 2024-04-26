from abc import abstractmethod
from .vector2d import vector2d


class ETKBaseObject:
    def __init__(self, pos: vector2d, size: vector2d) -> None:
        self._pos: vector2d = pos
        self._size: vector2d = size
    
    @property
    def pos(self) -> vector2d:
        return self._pos
    
    @pos.setter
    @abstractmethod
    def pos(self, value: vector2d) -> None:
        pass
    
    @property
    def _abs_pos(self) -> vector2d:
        """READ-ONLY"""
        return self._pos

    @property
    def size(self) -> vector2d:
        return self._size
    
    @size.setter
    @abstractmethod
    def size(self, value: vector2d):
        pass