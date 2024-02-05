from typing import Any
import TGMainWindow
from TGCanvasItem import *
from TGButton     import *
from TGLabel      import *
from TGCheckbox   import *
from TGEdit       import *
from TGTimer import TGTimer
import math


class GUI(TGMainWindow.TGMainWindow):
    def __init__(self) -> None:
        super().__init__(posX=0, posY=40, width=1540, height=768)
    
    def add_elements(self):
        self.myBtn2 = TGButton(self.object_id, "BTN2", 150, 0)
        self.myBtn2.add_event(ButtonEvents.BTN_PRESSED, self.ev_btn2)
        self.myBtn2.add_event(BaseEvents.MOUSE_DOWN, self.ev_btn_MD)
        self.my_tri:TGCanvasItem = self.canvas.draw_oval(vector2d(150,150), 50, 25)
        self.myBtn = TGButton(self.object_id, "BTN", 0, 0)
        self.myBtn.add_event(BaseEvents.MOUSE_DOWN, self.ev_btn)
        #self.myBtn.add_event(ButtonEvents.EV_BTN_PRESSED, self.ev_btn)

    def ev_btn_MD(self):
        print("hi")

    def ev_btn(self):
        self.myBtn2.dissable()
    
    def ev_btn2(self, params):
        print("hello")
    
    def ev_btn22(self, event):
        print("mouse down 2")

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