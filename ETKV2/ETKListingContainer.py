from enum import Enum, auto
from tkinter import Tk
from typing import Optional
from .Internal.ETKBaseContainer import Alignments
from .Internal.ETKBaseWidget import ETKBaseWidget
from .ETKContainer import ContainerSize
from .vector2d import vector2d
from .Internal.ETKBaseContainer import ETKBaseContainer, _SubAlignments, SizeError  # type:ignore

# TODO: insert, padding


class ElementPosLockedError(AttributeError):
    pass


class ListingTypes(Enum):
    TOP_TO_BOTTOM = auto()
    BOTTOM_TO_TOP = auto()
    LEFT_TO_RIGHT = auto()
    RIGHT_TO_LEFT = auto()


class ETKListingContainer(ETKBaseContainer):
    def __init__(self, tk: Tk, pos: vector2d = vector2d(0, 0), size: ContainerSize = ContainerSize(0, 0, True, True), alignment: Alignments = Alignments.TOP_LEFT, listing_type: ListingTypes = ListingTypes.TOP_TO_BOTTOM, offset: int = 10, background_color: int = 11184810, outline_color: Optional[int] = None) -> None:
        self.__alignment = alignment
        self.__listing_type = listing_type
        self.__offset = offset
        ETKBaseContainer.__init__(
            self, tk, pos, size, background_color, outline_color)

    # region Properties

    @ETKBaseContainer.size.setter
    def size(self, value: ContainerSize | vector2d) -> None:
        ETKBaseContainer.size.fset(self, value)  # type:ignore
        self._update_all_element_pos()

    # endregion
    # region Methods

    def _update_all_element_pos(self) -> None:
        if self.__listing_type in [ListingTypes.TOP_TO_BOTTOM, ListingTypes.BOTTOM_TO_TOP]:
            listing_dir_index = 1
            non_listing_dir_index = 0
        else:
            listing_dir_index = 0
            non_listing_dir_index = 1

        elements = [e for e in self._element_rel_pos.keys() if e.abs_enabled]
        sizes = [e.size for e in elements]

        if len(elements) == 0:
            return

        listing_dir_size = sum([s[listing_dir_index]
                               for s in sizes]) + self.__offset * (len(sizes) - 1)
        non_listing_dir_size = max([s[non_listing_dir_index] for s in sizes])

        needed_size = vector2d()
        needed_size[listing_dir_index] = listing_dir_size
        needed_size[non_listing_dir_index] = non_listing_dir_size

        if self.size.dynamic_x:
            self._container_size.x = int(needed_size.x)
        if self.size.dynamic_y:
            self._container_size.y = int(needed_size.y)

        # print(needed_size, self.size)

        ETKBaseContainer.size.fset(self, self.size)  # type:ignore

        # print(needed_size, self.size)

        if listing_dir_size > self.size[listing_dir_index] or non_listing_dir_size > self.size[non_listing_dir_index]:
            raise SizeError(
                f"size of container {self} is too small\ncontainer: size: {self.size}; needed: {needed_size}")

        listing_dir_pos = self.__calculate_pos_part(
            listing_dir_index, listing_dir_size)

        if self.__listing_type in [ListingTypes.BOTTOM_TO_TOP, ListingTypes.RIGHT_TO_LEFT]:
            elements = elements[::-1]

        for e in elements:
            non_listing_dir_pos = self.__calculate_pos_part(
                non_listing_dir_index, e.size[non_listing_dir_index])
            pos = vector2d()
            pos[listing_dir_index] = listing_dir_pos
            pos[non_listing_dir_index] = non_listing_dir_pos
            self._element_rel_pos[e] = pos
            e._pos = pos
            e._update_pos()
            listing_dir_pos += e.size[listing_dir_index] + self.__offset

    def __calculate_pos_part(self, index: int, size_part: float) -> float:
        match self.__alignment.value[index]:
            case _SubAlignments.MIN:
                return 0
            case _SubAlignments.MIDDLE:
                return 0.5 * self.size[index] - 0.5 * size_part
            case _SubAlignments.MAX:
                return self.size[index] - size_part

    # region child validation methods

    def _validate_pos(self, element: ETKBaseWidget) -> None:
        raise ElementPosLockedError(
            f"pos of element {element} is locked by ListingContainer {self}")

    # endregion
    # endregion