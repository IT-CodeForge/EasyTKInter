from TGBaseWidget import TGBaseWidget, BaseEvents
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
        self.__event_funcs:dict[EditEvents, Callable[...,None]] = {}
        self.__event_trans:dict[EditEvents, list[str|Callable[...,None]]] = {
                            EditEvents.EV_CHANGED:["<KeyPress>", self.__ev_changed, ""]}

    
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


    def add_event(self, event_type:EditEvents|BaseEvents, eventhandler:Callable[...,None]):
        if type(event_type) == EditEvents:
            self.__event_funcs[event_type] = eventhandler #type:ignore
            self.__event_trans[event_type][2] = self.object_id.bind(self.__event_trans[event_type][0], self.__event_trans[event_type][1]) #type:ignore
        elif type(event_type) == BaseEvents:
            super().add_event(event_type, eventhandler) #type:ignore
        else:
            raise ValueError(f"add_event of Button can only handle events of type BaseEvents and EditEvents. {type(event_type)} is not supported")

    def remove_event(self, event_type:EditEvents|BaseEvents):
        if type(event_type) == EditEvents:
            self.object_id.unbind(event_type, funcid=self.__event_trans[event_type][2]) #type:ignore
            self.__event_funcs.pop(event_type) #type:ignore
        elif type(event_type) == BaseEvents:
            super().remove_event(event_type) #type:ignore
        else:
            raise ValueError(f"remove_event of Button can only handle events of type BaseEvents and EditEvents. {type(event_type)} is not supported")
        
    def __ev_changed(self, event:Event):
        super()._handle_event(self.__event_funcs[EditEvents.EV_CHANGED],EditEvents.EV_CHANGED,event)


"""
    def __ev_input(self, event:Event):
        if event.char[1:-1] in self.__input_ev_chars:
            func:function = self.__event_funcs[EditEvents.EV_INPUT]
            std_arg_len = self.is_class_method(func)
            if func.__code__.co_argcount == std_arg_len:
                func()
            elif func.__code__.co_argcount == std_arg_len + 1:
                params = {"object_id":self.object_id,"event_type":EditEvents.EV_INPUT,"event":event,"mousepos":vector2d(event.x,event.y)}
                func(params)
            else:
                raise BaseException(f"the event method can only have one parameter in addition to the class. The given function {func.__name__} has {func.__code__.co_argcount - std_arg_len} parameters to many, parameter list: {func.__code__.co_varnames}")
"""