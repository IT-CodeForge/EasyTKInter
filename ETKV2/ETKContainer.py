from __future__ import annotations
from typing import Literal
from ETKV2.ETKBaseWidget import ETKBaseWidget

from ETKV2.vector2d import vector2d

from .ETKBaseContainer import Alignments, _SubAlignments, ContainerSize, ElementAlreadyAddedError, AddContainerToItselfError, ElementNotPartOfContainerError, SizeError, PosError, ETKBaseContainer #type:ignore


class ETKContainer(ETKBaseContainer):
    def __init__(self, pos: vector2d = vector2d(0, 0), size: ContainerSize = ContainerSize(0, 0, True, True), background_color: int = 11184810) -> None:
        super().__init__(pos, size, background_color)
    
    def add_element(self, element: ETKBaseWidget, alignment: Alignments = Alignments.TOP_LEFT):
        super().add_element(element, alignment)
        self._validate_size_pos(element.abs_pos, element.size)
        element._update_pos()
    
    def _calculate_abs_element_pos(self, child: ETKBaseWidget, index: Literal[0, 1]) -> float:
        print(index, (self.abs_pos[index], self.size[index]), (
            child.pos[index], child.size[index]), self._elements[child].value[index])
        match self._elements[child].value[index]:
            case _SubAlignments.MIN:
                return self.abs_pos[index] + child.pos[index]
            case _SubAlignments.MIDDLE:
                return self.abs_pos[index] + 0.5 * self.size[index] - 0.5 * child.size[index] + child.pos[index]
            case _SubAlignments.MAX:
                return self.abs_pos[index] + self.size[index] - child.size[index] + child.pos[index]
            
    def _update_size(self) -> None:
        if self._container_size.dynamic_x:
            self._container_size.x = int(
                max([e.pos.x + e.size.x for e in self._elements.keys()]))
        if self._container_size.dynamic_y:
            self._container_size.y = int(
                max([e.pos.y + e.size.y for e in self._elements.keys()]))
        ETKBaseContainer.size.fset(
            self, self._container_size.vec) # type:ignore