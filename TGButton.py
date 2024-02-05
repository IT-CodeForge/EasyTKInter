from abc import abstractmethod
from typing import Any, Callable
from enum         import Enum, auto
from TGBaseWidget import TGBaseWidget
from TGBaseObject import BaseEvents
from vector2d     import vector2d
from tkinter      import Button, Event, Tk

class ButtonEvents(Enum):
    BTN_PRESSED        = auto()
    BTN_RELEASED       = auto()

class TGButton(TGBaseWidget):
    def __init__(self, myTk:Tk, txt:str, posX:int, posY:int, width:int=80, height:int=17) -> None:
        self.object_id:Button = Button(myTk, text=txt, bg='#EEEEEE', fg='#000000')
        super().__init__(vector2d(posX, posY), vector2d(width, height))
        self.__event_trans:dict[ButtonEvents, str] = {
            ButtonEvents.BTN_PRESSED:"<ButtonPress>",
            ButtonEvents.BTN_RELEASED:"<ButtonRelease>"
        }
        self.__event_truth_funcs:dict[ButtonEvents, str] = {
            ButtonEvents.BTN_PRESSED:lambda event, object_id: object_id.cget("state") != "disabled",
            ButtonEvents.BTN_RELEASED:lambda event, object_id: object_id.cget("state") != "disabled"
        }

    @property
    def text(self)->str:
        return self.object_id.cget("text")
    
    @text.setter
    def text(self, value:str):
        self.object_id.config(text=value)
    
    def add_event(self, event_type: BaseEvents, eventhandler: Callable[..., None]):
        if type(event_type) == ButtonEvents:
            super().add_event(event_type, eventhandler, self.__event_trans[event_type], self.__event_truth_funcs[event_type])
        elif type(event_type) == BaseEvents:
            super().add_event(event_type, eventhandler)
        else:
            #Raise Error
            pass    
    
    def remove_event(self, event_type: BaseEvents):
        if type(event_type) == ButtonEvents:
            super().remove_event(event_type, self.__event_trans[event_type])
        elif type(event_type) == BaseEvents:
            super().remove_event(event_type)
        else:
            #Raise Error
            pass