from time import perf_counter
from typing import Any
import BMainWindow
from BCanvasItem import *
from BButton     import *
from BLabel      import *
from BCheckbox   import *
from BEdit       import *
from BTimer      import TGTimer
from BContainer  import *
from BListingContainer import *
from BBitmap     import *
import math

class GUI(BMainWindow.BMainWindow):
    def __init__(self) -> None:
        self.my_lines = []
        super().__init__(pos_x=0, pos_y=40, width=1540, height=768)
    
    def add_elements(self):
        self.myLbl = BLabel(self.object_id, "HHHHHHHHHHHHHHHHHHHHHHHHHH", 100, 300, 1000,500)
        self.myBtn2 = BButton(self.object_id, "BTN2")
        self.myBtn2.add_event(ButtonEvents.BTN_PRESSED, self.ev_btn2)
        self.myBtn = BButton(self.object_id, "BTN")
        self.myBtn.add_event(BaseEvents.MOUSE_DOWN, self.process)
        self.myBtn3 = BButton(self.object_id, "BTN3", 90, 27)
        self.myBtn3.add_event(BaseEvents.MOUSE_DOWN, self.ev_btn)
        self.myCon = BListingContainer(listing_type=ListingTypes.LEFT_TO_RIGHT)
        self.myCon.pos = self.myLbl.pos
        self.myCon2 = BContainer(self.myLbl)
        self.myCon.elements = [self.myBtn, self.myBtn2]
        self.myCon2.add_element(self.myBtn3, Alignments.MIDDLE_LEFT)
        self.my_oval_1 = self.canvas.draw_oval(vector2d(125,75), 100, 50, None)
        self.my_oval_2 = self.canvas.draw_oval(vector2d(200,75), 100, 50, None)
        self.my_oval_2.move(vector2d(-40,0))
        self.my_oval_2.rotate_with_degrees(-45)
        sol = self.my_oval_1.ray_casting(vector2d(125,0), vector2d(0,1))
        #print([str(e) for e in sol])



    def ev_btn(self):
        self.myBtn.visible = False
    
    def ev_btn2(self, params):
        self.myBtn.visible = True
        #self.myBtn.enabled = not self.myBtn.enabled

    def ev_chb(self, params:dict[str,Any]):
        if params.get("event_type", "") == CheckboxEvents.EV_CHECKED:
            self.my_tri.rotate_with_degrees(45)
        elif params.get("event_type", "") == CheckboxEvents.EV_UNCHECKED:
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

        

if __name__ == '__main__':
  w = GUI()
  w.run()