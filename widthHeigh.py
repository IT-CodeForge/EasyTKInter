import ETK.ETKMainWindow

class GUI(ETK.ETKMainWindow.ETKMainWindow):
    def __init__(self) -> None:
        self.my_lines = []
        super().__init__(pos_x=0, pos_y=40, width=200, height=200)
    
    def add_elements(self):
       pass

if __name__ == '__main__':
  w = GUI()
  w.run()