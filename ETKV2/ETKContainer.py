from __future__ import annotations
from enum import Enum, auto
from typing import Literal

from .ETKBaseWidgetDisableable import ETKBaseWidgetDisableable

from .ETKBaseWidget import ETKBaseWidget
from .vector2d import vector2d
from .ETKBaseWidgetDisableable import ETKBaseWidgetDisableable

# TODO: Events, bg_col, outline


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


class ContainerSize():
    def __init__(self, x: int, y: int, dynamic_x: bool = False, dynamic_y: bool = False) -> None:
        self.dynamic_x = dynamic_x
        self.dynamic_y = dynamic_y
        self.x = x
        self.y = y

    @property
    def x(self) -> int:
        return self.__x

    @x.setter
    def x(self, value: int) -> None:
        if not self.dynamic_x:
            self.__x = value

    @property
    def y(self) -> int:
        return self.__y

    @y.setter
    def y(self, value: int) -> None:
        if not self.dynamic_y:
            self.__y = value

    @property
    def dynamic_x(self) -> int:
        return self.__dynamic_x

    @dynamic_x.setter
    def dynamic_x(self, value: int) -> None:
        self.__dynamic_x = value
        if value:
            self.x = 0

    @property
    def dynamic_y(self) -> int:
        return self.__dynamic_y

    @dynamic_y.setter
    def dynamic_y(self, value: int) -> None:
        self.__dynamic_y = value
        if value:
            self.y = 0

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


class ETKContainer(ETKBaseWidgetDisableable):
    def __init__(self, pos: vector2d = vector2d(0, 0), size: ContainerSize = ContainerSize(0, 0, True, True), background_color: int = 11184810) -> None:
        ETKBaseWidgetDisableable.__init__(
            self, pos, size.vec)
        self.__elements: dict[ETKBaseWidget, Alignments] = {}
        self._container_size: ContainerSize = size

    @ETKBaseWidgetDisableable.pos.setter
    def pos(self, value: vector2d) -> None:
        ETKBaseWidget.pos.fset(self, value)  # type:ignore

    @property
    def size(self) -> ContainerSize:  # type:ignore
        return self._container_size

    @size.setter
    def size(self, value: ContainerSize | vector2d):
        if type(value) == ContainerSize:
            self._container_size = value
        else:
            self._container_size = ContainerSize(int(value.x), int(value.y))
        if self._container_size.dynamic_x:
            self._container_size.x = int(
                max([e.pos.x + e.size.x for e in self.__elements.keys()]))
        if self._container_size.dynamic_y:
            self._container_size.y = int(
                max([e.pos.y + e.size.y for e in self.__elements.keys()]))
        self.__validate_all_element_pos()
        ETKBaseWidgetDisableable.size.fset(
            self, self._container_size.vec)  # type:ignore

    def __validate_all_element_pos(self):
        for e in self.__elements.keys():
            self.__validate_element_pos(e)
    
    def __validate_element_pos(self, element: ETKBaseWidget):
        self.__validate_size_pos(element.abs_pos, element.size)

    def __validate_size_pos(self, abs_pos: vector2d, size: vector2d):
        s_a_pos = self.abs_pos
        s_size = self.size

        if s_size.x > self.size.x or s_size.y > self.size.y:
            raise SizeError(
                f"size is outside of container {self}\nparameter: abs_pos: {abs_pos}, size: {size}; container: abs_pos: {self.abs_pos}, size: {self.size}")

        if abs_pos.x + size.x > s_a_pos.x + s_size.x or abs_pos.y + size.y > s_a_pos.y + s_size.y or abs_pos.x < s_a_pos.x or abs_pos.y < s_a_pos.y:
            raise PosError(
                f"pos is outside of container {self}\nparameter: abs_pos: {abs_pos}, size: {size}; container: abs_pos: {self.abs_pos}, size: {self.size}")

    def add_element(self, element: ETKBaseWidget, alignment: Alignments = Alignments.TOP_LEFT):
        if element in self.__elements.keys():
            raise ElementAlreadyAddedError(
                f"element {element} is already in container {self}")
        if element == self:
            raise AddContainerToItselfError(
                f"cannot add container {self} to itself")

        element._parent = self
        self.__elements.update({element: alignment})
        self.__validate_element_pos(element)
        element._update_pos()

    def remove_element(self, element: ETKBaseWidget):
        if element not in self.__elements.keys():
            raise ElementNotPartOfContainerError(
                f"element {element} is not in container {self}")
        self.__elements.pop(element)
        element._parent = None
        element.pos = vector2d(0, 0)
        element._update_pos()

    def _get_childs_abs_pos(self, child: ETKBaseWidget) -> vector2d:
        if child not in self.__elements.keys():
            raise ElementNotPartOfContainerError(
                f"element {child} is not in container {self}")
        x = self.__calculate_abs_element_pos(child, 0)
        y = self.__calculate_abs_element_pos(child, 1)
        print(vector2d(x, y))
        return vector2d(x, y)

    def __calculate_abs_element_pos(self, child: ETKBaseWidget, index: Literal[0, 1]) -> float:
        print(index, (self.abs_pos[index], self.size[index]), (
            child.pos[index], child.size[index]), self.__elements[child].value[index])
        match self.__elements[child].value[index]:
            case _SubAlignments.MIN:
                return self.abs_pos[index] + child.pos[index]
            case _SubAlignments.MIDDLE:
                return self.abs_pos[index] + 0.5 * self.size[index] - 0.5 * child.size[index] + child.pos[index]
            case _SubAlignments.MAX:
                return self.abs_pos[index] + self.size[index] - child.size[index] + child.pos[index]

    def _validate_size(self, element: ETKBaseWidget):
        element._update_enabled()

    def _update_pos(self) -> None:
        for e in self.__elements.keys():
            e._update_pos()

    def detach_child(self, element: ETKBaseWidget):
        self.remove_element(element)
