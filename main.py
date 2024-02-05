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
        self.myBtn2.add_event(ButtonEvents.EV_BTN_PRESSED, self.ev_btn2)
        self.my_tri:TGCanvasItem = self.canvas.draw_oval(vector2d(150,150), 50, 25)
        self.myBtn = TGButton(self.object_id, "BTN", 0, 0)
        self.myBtn.add_event(ButtonEvents.EV_BTN_PRESSED, self.ev_btn)
        self.myLbl = TGLabel(self.object_id, "hello I am a Label", 10, 18, width=200)
        myChb = TGCheckbox(self.object_id, "Checkbox", 81, 0)
        myChb.add_event(CheckboxEvents.EV_CHECKED, self.ev_chb)
        myChb.add_event(CheckboxEvents.EV_UNCHECKED, self.ev_chb)
        self.myTmr = TGTimer(self.object_id, 500, self.process)

    def ev_btn(self):
        self.myLbl.replace_text("I am", "I'm")
    
    def ev_btn2(self):
        self.my_tri.move(vector2d(1,1))

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