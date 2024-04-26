import ETK.ETKMainWindow
from ETK.ETKButton import ETKButton, ButtonEvents
from ETK.ETKCanvas import ETKCanvas
from ETK.vector2d import vector2d
from tkinter import *

class GUI(ETK.ETKMainWindow.ETKMainWindow):
    def __init__(self) -> None:
        self.my_lines = []
        self.line_list = []
        super().__init__(pos_x=0, pos_y=40, width=200, height=200)
    
    def add_elements(self):
        self.canvas.width += 2
        self.canvas.height += 2
        self.line_list.append(self.canvas.draw_line(vector2d(0,200), vector2d(200,200), line_col=0xFF0000))
        self.line_list.append(self.canvas.draw_line(vector2d(200,0), vector2d(200,200), line_col=0xFF0000))


if __name__ == '__main__':
  w = GUI()
  w.run()

#offset (2,2)