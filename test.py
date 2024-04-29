from ETK import *


class GUI(ETKMainWindow):
    def __init__(self) -> None:
        super().__init__(caption="NENENE", background_color=0xFF0000)

    def _on_init(self) -> None:
        pass

    def _add_elements(self) -> None:
        self.container = ETKContainer(
            self._tk_object, size=ETKContainerSize(100, 100), outline_thickness=3, outline_color=0x0000FF, background_color=0x00FF00)
        self.container.outline_color = 0x0000FF
        self.label = ETKLabel(self._tk_object, "LABEL")
        #self.label.enabled = False
        self.container.add_element(self.label, ETKAlignments.TOP_RIGHT)
        self.label.outline_thickness = 2
        self.label.outline_color = 0xFFFF00
        # self.label.pos = vector2d(-10, 0)


if __name__ == '__main__':
    w = GUI()
    w.run()
