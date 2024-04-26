from time import perf_counter
from typing import Any
import ETK.ETKMainWindow
from ETK.ETKCanvasItem import *
from ETK.ETKButton     import *
from ETK.ETKLabel      import *
from ETK.ETKCheckbox   import *
from ETK.ETKEdit       import *
from ETK.ETKTimer      import ETKTimer
from ETK.ETKContainer  import *
from ETK.ETKListingContainer import *
from ETK.ETKBitmap     import *
import math

class GUI(ETK.ETKMainWindow.ETKMainWindow):
    def __init__(self) -> None:
        self.my_lines = []
        super().__init__(pos_x=0, pos_y=40, width=1540, height=768)
    
    def add_elements(self):
        self.bckgd = ETKLabel(self.object_id,pos_x=10, pos_y=20, width=100, height=200, fill=0x0000FF)
        self.lContainer = ETKListingContainer(self.bckgd)
        #self.lContainer.width = 100
        #self.lContainer.height = 200

        self.testlbl1 = ETKLabel(self.object_id, fill=0xFF0000, height=20)
        self.testlbl2 = ETKLabel(self.object_id, pos_y=50, fill=0x00FF00, height=20)
        self.lContainer.elements.append(self.testlbl1)
        self.lContainer.elements.append(self.testlbl2)
        print(self.testlbl1.pos)
        print(self.testlbl2.pos)
        



    def ev_btn(self):
        self.myBtn.visible = False
    
    def ev_btn2(self, params):
        self.myBtn.visible = True
        #self.myBtn.enabled = not self.myBtn.enabled

    def ev_chb(self, params:dict[str,Any]):
        if params.get("event_type", "") == CheckboxEvents.CB_CHECKED:
            self.my_tri.rotate_with_degrees(45)
        elif params.get("event_type", "") == CheckboxEvents.CB_UNCHECKED:
            self.my_tri.move(vector2d(1,1))
        else:
            print("ERROR")
    
    def process(self):
        for line in self.my_lines:
            line.delete()
        self.my_lines = []
        self.my_oval_2.rotate_with_degrees(10)
        sol = self.my_oval_1.find_intersections(self.my_oval_2)
        for vec in sol:
            self.my_lines.append(self.canvas.draw_line(vector2d(0,0), vec))
    
    def touch_canvas(self, params):
        my_event:Event = params.get("event")
        mouse_pos = vector2d(my_event.x,my_event.y)
        print(self.my_oval_1.is_point_in_shape(mouse_pos))

        

if __name__ == '__main__':
  w = GUI()
  w.run()