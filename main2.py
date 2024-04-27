#from ETKV2.ETKMainWindow import WindowEvents
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
        self.button.enabled = True
        #self.add_event(WindowEvents.MOUSE_MOVED, self.test4)
    
    def test(self):
        self.background_color = 0x00FF00
    
    def test2(self):
        print("BTN")

    def test3(self):
        print("BTN2")
    
    def test4(self):
        print("WIN")

        

if __name__ == '__main__':
  w = GUI()
  w.run()