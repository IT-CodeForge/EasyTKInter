from ETK import *


class GUI(ETKMainWindow):
    def __init__(self) -> None:
        super().__init__(caption="NENENE", background_color=0xFF0000, size=None, fullscreen=True)

    def _on_init(self) -> None:
        pass

    def _add_elements(self) -> None:
        self.checkbox = ETKCheckbox(self._tk_object, "Test")
        self.button = ETKButton(self._tk_object, pos=vector2d(0, 100))
        def x() -> None:
            self.checkbox.state = not self.checkbox.state
        self.button.add_event(ETKButtonEvents.PRESSED, x)
        self.checkbox.add_event(ETKCheckboxEvents.TOGGLED, lambda: print("TOGGLED"))
        self.checkbox.add_event(ETKCheckboxEvents.CHECKED, lambda: print("CHECKED"))
        self.checkbox.add_event(ETKCheckboxEvents.UNCHECKED, lambda: print("UNCHECKED"))


if __name__ == '__main__':
    w = GUI()
    w.run()
