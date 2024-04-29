from ETK import *


class GUI(ETKMainWindow):
    def __init__(self) -> None:
        super().__init__(caption="NENENE", background_color=0xFF0000, size=None, fullscreen=True)

    def _on_init(self) -> None:
        pass

    def _add_elements(self) -> None:
        self.label = ETKButton(self._tk_object, "test")
        self.label.outline_thickness = 3
        self.label.outline_color = 0x0
        print(self.label.text)
        self.label.text = "test123"
        print(self.label.text)


if __name__ == '__main__':
    w = GUI()
    w.run()
