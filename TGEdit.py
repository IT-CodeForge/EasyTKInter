from TGBaseWidget import TGBaseWidget
from TGBaseObject import BaseEvents
from typing   import Any, Callable
from enum     import Enum
from vector2d import vector2d
from tkinter  import Entry, END, Event, Tk

class EditEvents(Enum):
    EV_CHANGED = 0

class TGEdit(TGBaseWidget):
    def __init__(self, myTk:Tk, txt:str, posX:int, posY:int, width:int=80, height:int=17) -> None:
        self.object_id:Entry = Entry(myTk, bg='#FFFFFF', fg='#000000')
        self.object_id.insert(0,txt)
        super().__init__(vector2d(posX, posY), vector2d(width, height))
        self.__event_trans:dict[EditEvents, str] = {
            EditEvents.EV_CHANGED:"<KeyPress>"
        }
        self.__event_truth_funcs:dict[EditEvents, Callable[..., None]] = {
            EditEvents.EV_CHANGED:lambda event, object_id : object_id.cget("state") != "disabled"
        }

    
    @property
    def text(self)->str:
        return self.object_id.cget("text")
    
    @text.setter
    def text(self, value:str):
        self.object_id.delete(0,END)
        self.object_id.insert(0,value)
    
    def append_text(self, txt:str):
        self.text += txt
    
    def insert_text(self, index:int, txt:str):
        holdleft = self.text[:index]
        holdright = self.text[index:]
        self.text = holdleft + txt + holdright
    
    def insert_text_after(self, search_str:str, txt:str):
        search_str_index = self.text.find(search_str)
        self.insert_text(search_str_index + len(search_str), txt)
    
    def replace_text(self, replace_str:str, txt:str):
        self.text.replace(replace_str, txt)
    
    def delete_txt(self, startindex:int, endindex:int):
        self.replace_text(self.text[startindex:endindex], "")
    
    def delete_txt(self, del_str:str):
        self.replace_text(del_str, "")
    
    def add_event(self, event_type: BaseEvents, eventhandler: Callable[..., None]):
        if type(event_type) == EditEvents:
            super().add_event(event_type, eventhandler, self.__event_trans[event_type], self.__event_truth_funcs[event_type])
        elif type(event_type) == BaseEvents:
            super().add_event(event_type, eventhandler)
        else:
            #Raise Error
            pass    
    
    def remove_event(self, event_type: BaseEvents):
        if type(event_type) == EditEvents:
            super().remove_event(event_type, self.__event_trans[event_type])
        elif type(event_type) == BaseEvents:
            super().remove_event(event_type)
        else:
            #Raise Error
            pass