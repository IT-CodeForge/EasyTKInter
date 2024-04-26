import ETK.ETKMainWindow
from ETK.ETKButton import ETKButton, ButtonEvents
from ETK.vector2d import vector2d

class GUI(ETK.ETKMainWindow.ETKMainWindow):
    def __init__(self) -> None:
        self.my_lines = []
        super().__init__(pos_x=0, pos_y=40, width=200, height=200)
    
    def add_elements(self):
        self.btn =ETKButton(self.object_id)
        self.btn.add_event(ButtonEvents.BTN_PRESSED,self.test)
        print(self.canvas.width,self.canvas.height)
        for i in range(self.width//10):
            self.canvas.draw_line(vector2d(i*10,0), vector2d(i*10,200))
    
    def test(self):
        temp = self.canvas.draw_polygon([vector2d(0,0), vector2d(100,0), vector2d(100,100), vector2d(0,100)], fill_col=0xFF0000)
        print([str(e) for e in temp.pointlist])
        print(hex(temp.fill))


if __name__ == '__main__':
  w = GUI()
  w.run()