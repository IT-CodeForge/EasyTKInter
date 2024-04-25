import ETK.ETKMainWindow
from ETK.vector2d import vector2d

class GUI(ETK.ETKMainWindow.ETKMainWindow):
    def __init__(self) -> None:
        self.my_lines = []
        super().__init__(pos_x=0, pos_y=40, width=200, height=200)
    
    def add_elements(self):
        for i in range(self.width//10):
            self.canvas.draw_line(vector2d(i*10,0), vector2d(i*10,self.height))

if __name__ == '__main__':
  w = GUI()
  w.run()