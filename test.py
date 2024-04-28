from ETK import *

class GUI(ETKMainWindow):
    def __init__(self) -> None:
        super().__init__(caption="NENENE", background_color=0xFF0000)

    def _on_init(self) -> None:
        pass

    def _add_elements(self) -> None:
        self.label = ETKLabel(self._tk_object, "LABEL")
        self.button = ETKButton(self._tk_object)


if __name__ == '__main__':
    w = GUI()
    w.run()