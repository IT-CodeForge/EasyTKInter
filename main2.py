# from ETKV2.ETKMainWindow import WindowEvents
from ETKV2.ETKListingContainer import ETKListingContainer, ListingTypes
from ETKV2.ETKCheckbox import ETKCheckbox, CheckboxEvents
from ETKV2.ETKLabel import ETKLabel
from ETKV2.ETKEdit import ETKEdit, EditEvents
from ETKV2.Internal.ETKBaseTkObject import BaseEvents  # TODO
from ETKV2.vector2d import vector2d
from ETKV2.ETKButton import ETKButton, ButtonEvents
from ETKV2.ETKMainWindow import ETKMainWindow, WindowEvents
from ETKV2.ETKContainer import ETKContainer, ContainerSize, Alignments


class GUI(ETKMainWindow):
    def __init__(self) -> None:
        super().__init__(caption="NENENE", background_color=0xFF0000)

    def _on_init(self) -> None:
        pass  # print("INIT")

    def _add_elements(self) -> None:
        self.listingcontainer = ETKListingContainer(self._tk_object, vector2d(10, 10), ContainerSize(
            500, 100, True, True), Alignments.TOP_RIGHT, ListingTypes.RIGHT_TO_LEFT, background_color=0x00FF00)

        # self.color_label = ETKLabel(self._tk_object, "", self.listingcontainer.abs_pos, self.listingcontainer.size.vec, 0x00FF00)

        self.label1 = ETKEdit(self._tk_object, "LABEL1")
        self.label2 = ETKLabel(self._tk_object, "LABEL2")

        self.listingcontainer.add_element(self.label1)
        self.listingcontainer.add_element(self.label2)

        # self.color_label.size = self.listingcontainer.size.vec
        self.listingcontainer.visibility = True

        return
        self.add_event(BaseEvents.MOUSE_MOVED, lambda: print("MOVED"))
        self.label2 = ETKLabel(self._tk_object, "LABEL2")
        self.label2.add_event(BaseEvents.MOUSE_MOVED, lambda: print("MOVED2"))

        return

        return

        self.container = ETKContainer(self._tk_object, vector2d(
            0, 20), ContainerSize(200, 200, True, True))

        self.color_label = ETKLabel(self._tk_object, "", vector2d(
            0, 20), vector2d(100, 200), 0x00FF00)

        self.label = ETKLabel(self._tk_object, "LABEL", vector2d(-10, 30))

        self.container.add_element(self.label, Alignments.TOP_RIGHT)

        self.label.pos = vector2d(-400, 400)

        self.color_label.size = self.container.size.vec

        return

        # self._tk_object.after(2000, self.test)
        self.button = ETKButton(self._tk_object, "BTN", vector2d(
            0, 0), vector2d(100, 100), 0xAAAAAA, 0xFFFFFF)
        self.button.text_color = 0x0
        self.button.add_event(ButtonEvents.PRESSED, self.test2)
        self.button.add_event(BaseEvents.MOUSE_DOWN, self.test3)
        # self.button.enabled = False
        # self.button.visibility = False
        # self.add_event(WindowEvents.MOUSE_MOVED, self.test4)

        self.label = ETKLabel(self._tk_object, "LABEL", vector2d(100, 0))

        self.edit = ETKEdit(self._tk_object, "TEXT", vector2d(100, 20))
        self.edit.add_event(EditEvents.CHANGED, self.test5)
        self.edit.text += "1"

        self.checkbox = ETKCheckbox(
            self._tk_object, "CHECKBOX", vector2d(100, 40))
        self.checkbox.add_event(CheckboxEvents.TOGGLED, self.test6)

        self.add_event(WindowEvents.START, self.teststart)
        self.add_event(WindowEvents.EXIT, self.testexit)
        # self.topmost = True
        self.add_event(WindowEvents.FOCUS_IN, self.testfocin)
        self.add_event(WindowEvents.FOCUS_OUT, self.testfocout)

    # def test(self):
    #     self.background_color = 0x00FF00

    # def test2(self):
    #     print("BTN")
    #     self.edit.text += "1"

    # def test20(self):
    #     self.visibility = True

    # def test3(self):
    #     print("BTN2")

    # def test4(self):
    #     print("WIN")

    # def test5(self):
    #     print("EDIT")

    # def test6(self):
    #     print(self.checkbox.state)

    # def teststart(self):
    #     print("START")

    # def testexit(self):
    #     print("EXIT")

    # def testfocin(self):
    #     print("FOCIN")

    # def testfocout(self):
    #     print("FOCOUT")


if __name__ == '__main__':
    w = GUI()
    w.run()
