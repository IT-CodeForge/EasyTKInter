#from ETKV2.ETKMainWindow import WindowEvents
from ETKV2.ETKCheckbox import ETKCheckbox, CheckboxEvents
from ETKV2.ETKLabel import ETKLabel
from ETKV2.ETKEdit import ETKEdit, EditEvents
from ETKV2.ETKBaseTkObject import BaseEvents
from ETKV2.vector2d import vector2d
from ETKV2.ETKButton import ETKButton, ButtonEvents
from ETKV2.ETKMainWindow import ETKMainWindow

class GUI(ETKMainWindow):
    def __init__(self) -> None:
        super().__init__(caption="NENENE", background_color=0xFF0000)
    
    def _add_elements(self) -> None:
        #self._tk_object.after(2000, self.test)
        self.button = ETKButton(self._tk_object, "BTN", vector2d(0, 0), vector2d(100, 100), 0xAAAAAA, 0xFFFFFF)
        self.button.text_color = 0x0
        self.button.add_event(ButtonEvents.BUTTON_PRESSED, self.test2)
        self.button.add_event(BaseEvents.MOUSE_DOWN, self.test3)
        #self.button.enabled = False
        #self.button.visibility = False
        #self.add_event(WindowEvents.MOUSE_MOVED, self.test4)

        self.label = ETKLabel(self._tk_object, "LABEL", vector2d(100, 0))

        self.edit = ETKEdit(self._tk_object, "TEXT", vector2d(100, 20))
        self.edit.add_event(EditEvents.EV_CHANGED, self.test5)
        self.edit.text += "1"

        self.checkbox = ETKCheckbox(self._tk_object, "CHECKBOX", vector2d(100, 40))
        self.checkbox.add_event(CheckboxEvents.CB_TOGGLED, self.test6)
    
    def test(self):
        self.background_color = 0x00FF00
    
    def test2(self):
        print("BTN")
        self.edit.text += "1"
    
    def test20(self):
        self.visibility = True

    def test3(self):
        print("BTN2")
    
    def test4(self):
        print("WIN")
    
    def test5(self):
        print("EDIT")
    
    def test6(self):
        print(self.checkbox.state)

        

if __name__ == '__main__':
  w = GUI()
  w.run()