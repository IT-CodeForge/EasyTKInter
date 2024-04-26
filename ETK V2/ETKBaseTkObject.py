from typing import Any, Optional
from .vector2d import vector2d
from .ETKBaseObject import ETKBaseObject
from .ETKUtils import gen_col_from_int

class ETKBaseTkObject(ETKBaseObject):
    def __init__(self, pos: vector2d, size: vector2d, background_color: int = 0xAAAAAA) -> None:
        super().__init__(pos, size)
        self._tk_object: Any
        self.background_color = background_color #NOTE: muss nach child init passieren!
    
    @property
    def background_color(self) -> int:
        return int(self._background_color[1:], 16)
    
    @background_color.setter
    def background_color(self, value: Optional[int]) -> None:
        self._background_color = gen_col_from_int(value)
        self._tk_object.configure(background='#AAAAAA')