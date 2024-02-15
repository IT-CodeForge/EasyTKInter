from typing       import Any, Callable
from enum         import Enum, auto
from TGBaseWidget import TGBaseWidget
from TGBaseObject import BaseEvents
from vector2d     import vector2d
from tkinter      import Event, IntVar, Tk, Checkbutton

class CheckboxEvents(Enum):
    EV_CHECKED   = auto()
    EV_UNCHECKED = auto()
    EV_TOGGLED   = auto()

class TGCheckbox(TGBaseWidget):
    def __init__(self, myTk:Tk, txt:str="", pos_x:int=0, pos_y:int=0, width:int=80, height:int=17) -> None:
        self.__state = IntVar()
        self.object_id:Checkbutton = Checkbutton(myTk, text=txt, bg='#EEEEEE', fg='#000000', variable=self.__state)
        super().__init__(vector2d(pos_x, pos_y), vector2d(width, height))
        self.__event_funcs:dict[CheckboxEvents, Callable[...,None]] = {}
        self.__event_trans:dict[CheckboxEvents, str] = {
            CheckboxEvents.EV_CHECKED:"<ButtonPressed>",
            CheckboxEvents.EV_UNCHECKED:"<ButtonPressed>",
            CheckboxEvents.EV_TOGGLED:"<ButtonPressed>"
        }
        self.__event_truth_funcs:dict[CheckboxEvents, Callable[..., None]] = {
            CheckboxEvents.EV_CHECKED:lambda event, object_id : object_id.cget("state") == "normal",
            CheckboxEvents.EV_UNCHECKED:lambda event, object_id : object_id.cget("state") == "active",
            CheckboxEvents.EV_TOGGLED:lambda event, object_id : object_id.cget("state") != "disabled"
        }

    @property
    def state(self) -> bool:
        return bool(self.__state.get())

    @state.setter
    def state(self, value: bool):
        self.__state.set(value)

    @property
    def text(self)->str:
        return self.object_id.cget("text")
    
    @text.setter
    def text(self, value:str):
        self.object_id.config(text=value)
    
    def add_event(self, event_type: BaseEvents, eventhandler: Callable[..., None]):
        if type(event_type) == CheckboxEvents:
            super().add_event(event_type, eventhandler, self.__event_trans[event_type], self.__event_truth_funcs[event_type])
        elif type(event_type) == BaseEvents:
            super().add_event(event_type, eventhandler)
        else:
            #Raise Error
            pass    
    
    def remove_event(self, event_type: BaseEvents, eventhandler:Callable[..., None]):
        if type(event_type) == CheckboxEvents:
            super().remove_event(event_type, eventhandler, self.__event_trans[event_type])
        elif type(event_type) == BaseEvents:
            super().remove_event(event_type, eventhandler)
        else:
            #Raise Error
            pass 

#event routing functions       
    def __event(self, event:Event):
        checkbox_state = not self.__state.get() #needs to be inverted, since state update happens after event call
        if self.__event_funcs.get(CheckboxEvents.EV_TOGGLED, None) != None and self.object_id["state"] == "normal":
            super()._handle_event(self.__event_funcs[CheckboxEvents.EV_TOGGLED],CheckboxEvents.EV_TOGGLED,event)
        if checkbox_state and self.__event_funcs.get(CheckboxEvents.EV_CHECKED, None) != None and self.object_id["state"] == "normal":
            super()._handle_event(self.__event_funcs[CheckboxEvents.EV_CHECKED],CheckboxEvents.EV_CHECKED,event)
        if not checkbox_state and self.__event_funcs.get(CheckboxEvents.EV_UNCHECKED, None) != None and self.object_id["state"] == "normal":
            super()._handle_event(self.__event_funcs[CheckboxEvents.EV_UNCHECKED],CheckboxEvents.EV_UNCHECKED,event)