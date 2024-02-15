from time import perf_counter
from typing import Any
import TGMainWindow
from TGCanvasItem import *
from TGButton     import *
from TGLabel      import *
from TGCheckbox   import *
from TGEdit       import *
from TGTimer      import TGTimer
from TGContainer  import *
from TGListingContainer import *
from TGBitmap     import *
import math


class GUI(TGMainWindow.TGMainWindow):
    def __init__(self) -> None:
        super().__init__(pos_x=0, pos_y=40, width=1540, height=768)
    
    def add_elements(self):
        self.myLbl = TGLabel(self.object_id, "HALLO\nmultiline", 100, 300, 1000,500)
        self.myBtn2 = TGButton(self.object_id, "BTN2")
        self.myBtn2.add_event(ButtonEvents.BTN_PRESSED, self.ev_btn2)
        self.myBtn = TGButton(self.object_id, "BTN")
        self.myBtn3 = TGButton(self.object_id, "BTN3", 90, 27)
        self.myBtn3.add_event(BaseEvents.MOUSE_DOWN, self.ev_btn)
        self.myCon = TGListingContainer(self.myLbl, listing_type=ListingTypes.LEFT_TO_RIGHT)
        self.myCon2 = TGContainer(self.myLbl)
        self.myCon.elements = [self.myBtn, self.myBtn2]
        self.myCon2.add_element(self.myBtn3, Alignments.MIDDLE_LEFT)
        self.my_oval_1 = self.canvas.draw_oval(vector2d(125,75), 100, 50, -1)
        self.my_oval_2 = self.canvas.draw_oval(vector2d(200,75), 100, 50, -1)
        self.my_oval_2.move(vector2d(0,0))
        start = perf_counter()
        sol = self.my_oval_1.find_intersections(self.my_oval_2)
        end = perf_counter()
        print(end-start)
        print([str(x) for x in sol])
        for vec in sol:
            self.canvas.draw_line(vector2d(0,0), vec)



    def ev_btn(self):
        self.myBtn.visible = False
    
    def ev_btn2(self, params):
        self.myBtn.visible = True

    def ev_chb(self, params:dict[str,Any]):
        if params.get("event_type", "") == CheckboxEvents.EV_CHECKED:
            self.my_tri.rotate_with_degrees(45)
        elif params.get("event_type", "") == CheckboxEvents.EV_UNCHECKED:
            self.my_tri.move(vector2d(1,1))
        else:
            print("ERROR")
    
    def process(self):
        pass

        

if __name__ == '__main__':
  w = GUI()
  w.run()