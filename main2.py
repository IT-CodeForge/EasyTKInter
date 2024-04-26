from ETKV2.vector2d import vector2d
from ETKV2.ETKButton import ETKButton
from ETKV2.ETKMainWindow import ETKMainWindow

class GUI(ETKMainWindow):
    def __init__(self) -> None:
        super().__init__(caption="NENENE", background_color=0xFF0000)
    
    def add_elements(self):
        #self._tk_object.after(2000, self.test)
        self.button = ETKButton(self._tk_object, "BTN", vector2d(0, 0), vector2d(100, 100))
    
    def test(self):
        self.background_color = 0x00FF00

        

if __name__ == '__main__':
  w = GUI()
  w.run()