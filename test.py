from ETK import *


class GUI(ETKMainWindow):
    def __init__(self) -> None:
        super().__init__(scheduler_disabled=True)

    def _on_init(self) -> None:
        pass

    def _add_elements(self) -> None:
        pass


if __name__ == '__main__':
    w = GUI()
    w.run()
