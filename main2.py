from ETKV2.ETKBaseTkObject import BaseEvents
from ETKV2.vector2d import vector2d
from ETKV2.ETKButton import ETKButton, ButtonEvents
from ETKV2.ETKMainWindow import ETKMainWindow

class GUI(ETKMainWindow):
    def __init__(self) -> None:
        super().__init__(caption="NENENE", background_color=0xFF0000)
    
    def add_elements(self):
        #self._tk_object.after(2000, self.test)
        self.button = ETKButton(self._tk_object, "BTN", vector2d(0, 0), vector2d(100, 100))
        self.button.add_event(ButtonEvents.BUTTON_PRESSED, self.test2)
        self.button.add_event(BaseEvents.MOUSE_DOWN, self.test3)
        self.button._enabled = True
    
    def test(self):
        self.background_color = 0x00FF00
    
    def test2(self):
        print("BTN")

    def test3(self):
        print("BTN2")

        

if __name__ == '__main__':
  w = GUI()
  w.run()