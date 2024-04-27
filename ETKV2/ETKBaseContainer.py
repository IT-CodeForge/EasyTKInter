from abc import abstractmethod
from enum import Enum, auto
from typing import Literal
from .ETKBaseWidget import ETKBaseWidget
from .vector2d import vector2d
from .ETKBaseWidgetDisableable import ETKBaseWidgetDisableable

# TODO: Events, bg_col, outline, enabled, visible, padding bei dynamic size

# region Enums


class _SubAlignments(Enum):
    MIN = auto()
    MIDDLE = auto()
    MAX = auto()


class Alignments(Enum):  # NOTE
    TOP_LEFT = (_SubAlignments.MIN, _SubAlignments.MIN)
    TOP_CENTER = (_SubAlignments.MIDDLE, _SubAlignments.MIN)
    TOP_RIGHT = (_SubAlignments.MAX, _SubAlignments.MIN)
    MIDDLE_LEFT = (_SubAlignments.MIN, _SubAlignments.MIDDLE)
    MIDDLE_CENTER = (_SubAlignments.MIDDLE, _SubAlignments.MIDDLE)
    MIDDLE_RIGHT = (_SubAlignments.MAX, _SubAlignments.MIDDLE)
    BOTTOM_LEFT = (_SubAlignments.MIN, _SubAlignments.MAX)
    BOTTOM_CENTER = (_SubAlignments.MIDDLE, _SubAlignments.MAX)
    BOTTOM_RIGHT = (_SubAlignments.MAX, _SubAlignments.MAX)

# endregion

# region Dataclass: ContainerSize


class ContainerSize():
    def __init__(self, x: int, y: int, dynamic_x: bool = False, dynamic_y: bool = False) -> None:
        self.dynamic_x = dynamic_x
        self.dynamic_y = dynamic_y
        self.x = x
        self.y = y

    @property
    def vec(self) -> vector2d:
        """READ-ONLY"""
        return vector2d(self.x, self.y)

    def __str__(self) -> str:
        return f"<{self.x}, {self.y}, {self.dynamic_x}, {self.dynamic_y}>"

    def __setitem__(self, address: int, other: int) -> None:
        if address not in [0, 1, 2, 3]:
            raise KeyError("Invalid index")
        match address:
            case 0:
                self.x = other
            case 1:
                self.y = other
            case 2:
                self.dynamic_x = other
            case 3:
                self.dynamic_y = other
            case _:
                pass

    def __getitem__(self, address: int) -> int:
        if address not in [0, 1, 2, 3]:
            raise KeyError("Invalid index")
        match address:
            case 0:
                return self.x
            case 1:
                return self.y
            case 2:
                return self.dynamic_x
            case 3:
                return self.dynamic_y
            case _:
                raise KeyError

# endregion

# region ExceptionTypes


class ElementAlreadyAddedError(ValueError):
    pass


class AddContainerToItselfError(ValueError):
    pass


class ElementNotPartOfContainerError(ValueError):
    pass


class SizeError(ValueError):
    pass


class PosError(ValueError):
    pass

# endregion


class ETKBaseContainer(ETKBaseWidgetDisableable):
    def __init__(self, pos: vector2d = vector2d(0, 0), size: ContainerSize = ContainerSize(0, 0, True, True), background_color: int = 11184810) -> None:
        ETKBaseWidgetDisableable.__init__(
            self, pos, size.vec)
        self._element_rel_pos: dict[ETKBaseWidget, vector2d] = {}
        self._container_size: ContainerSize = size

    @property
    def size(self) -> ContainerSize:  # type:ignore
        return self._container_size

    @size.setter
    def size(self, value: ContainerSize | vector2d):
        if type(value) == ContainerSize:
            self._container_size = value
        else:
            self._container_size = ContainerSize(int(value.x), int(value.y))

    def add_element(self, element: ETKBaseWidget):
        if element in self._element_rel_pos.keys():
            raise ElementAlreadyAddedError(
                f"element {element} is already in container {self}")
        if element == self:
            raise AddContainerToItselfError(
                f"cannot add container {self} to itself")

        element._parent = self

        self._element_rel_pos.update({element: vector2d()})

    def remove_element(self, element: ETKBaseWidget):
        if element not in self._element_rel_pos.keys():
            raise ElementNotPartOfContainerError(
                f"element {element} is not in container {self}")
        self._element_rel_pos.pop(element)
        element._parent = None
        element.pos = vector2d(0, 0)
        element._update_pos()

    def _get_childs_abs_pos(self, child: ETKBaseWidget) -> vector2d:
        if child not in self._element_rel_pos.keys():
            raise ElementNotPartOfContainerError(
                f"element {child} is not in container {self}")
        return self._calculate_abs_pos(child)

    def _calculate_abs_pos(self, child: ETKBaseWidget) -> vector2d:
        pos = self._element_rel_pos[child]
        return vector2d(pos.x + self.abs_pos.x, pos.y + self.abs_pos.y)
    
    def _calculate_rel_element_pos(self, element: ETKBaseWidget) -> vector2d:
        x = self._calculate_rel_element_pos_part(element, 0)
        y = self._calculate_rel_element_pos_part(element, 1)
        return vector2d(x, y)

    @abstractmethod
    def _calculate_rel_element_pos_part(self, element: ETKBaseWidget, index: Literal[0, 1]) -> float:
        pass

    def _validate_size(self, element: ETKBaseWidget):
        element._update_pos()

    def _update_pos(self) -> None:
        for e in self._element_rel_pos.keys():
            e._update_pos()

    def _detach_child(self, element: ETKBaseWidget):
        self.remove_element(element)
