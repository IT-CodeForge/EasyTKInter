from ETK import *


class GUI(ETKMainWindow):
    def __init__(self) -> None:
        super().__init__(caption="NENENE", background_color=0xFF0000, size=None, fullscreen=True)

    def _on_init(self) -> None:
        pass

    def _add_elements(self) -> None:
        self.checkbox = ETKCheckbox(self._tk_object, "Test", vector2d(0, 40))
        self.edit = ETKEdit(self._tk_object, "Test", vector2d(0, 0))
        self.edit2 = ETKEdit(self._tk_object, "Test2", vector2d(0, 20))
        self.edit.add_event(ETKEditEvents.CHANGED, lambda: print(f"CHANGED {self.edit.text}"))
        self.edit.add_event(ETKEditEvents.CHANGED_DELAYED, lambda: print(f"CHANGED_DELAYED {self.edit.text}"))
        self.button = ETKButton(self._tk_object, pos=vector2d(0, 60))
        
        def x() -> None:
            self.edit.text += "1"
        self.button.add_event(ETKButtonEvents.PRESSED, x)


if __name__ == '__main__':
    w = GUI()
    w.run()
