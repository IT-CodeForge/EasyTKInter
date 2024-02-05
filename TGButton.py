from abc import abstractmethod
from typing import Any, Callable
from enum         import Enum
from TGBaseWidget import BaseEvents, TGBaseWidget
from vector2d     import vector2d
from tkinter      import Button, Event, Tk

class ButtonEvents(Enum):
    EV_BTN_PRESSED        = 0
    EV_BTN_RELEASED       = 1
    EV_BTN_DOUBLE_PRESSED = 2

class TGButton(TGBaseWidget):
    def __init__(self, myTk:Tk, txt:str, posX:int, posY:int, width:int=80, height:int=17) -> None:
        self.object_id:Button = Button(myTk, text=txt, bg='#EEEEEE', fg='#000000')
        super().__init__(vector2d(posX, posY), vector2d(width, height))
        self.__event_funcs:dict[ButtonEvents, Callable[...,None]] = {}
        self.__event_trans:dict[ButtonEvents, list[str|Callable[...,None]]] = {
                            ButtonEvents.EV_BTN_PRESSED:["<Button-1>", self.__ev_pressed, ""],
                            ButtonEvents.EV_BTN_RELEASED:["<ButtonRelease-1>", self.__ev_released, ""],
                            ButtonEvents.EV_BTN_DOUBLE_PRESSED:["<Double-Button-1>",self.__ev_double_pressed, ""]}

    @property
    def text(self)->str:
        return self.object_id.cget("text")
    
    @text.setter
    def text(self, value:str):
        self.object_id.config(text=value)

#events
    def add_event(self, event_type:ButtonEvents|BaseEvents, eventhandler:Callable[...,None]):
        if type(event_type) == ButtonEvents:
            self.__event_funcs[event_type] = eventhandler #type:ignore
            self.__event_trans[event_type][2] = self.object_id.bind(self.__event_trans[event_type][0], self.__event_trans[event_type][1]) #type:ignore
        elif type(event_type) == BaseEvents:
            super().add_event(event_type, eventhandler) #type:ignore
        else:
            raise ValueError(f"add_event of Button can only handle events of type BaseEvents and ButtonEvents. {type(event_type)} is not supported")



    def remove_event(self, event_type:ButtonEvents|BaseEvents):
        if type(event_type) == ButtonEvents:
            self.object_id.unbind(self.__event_trans[event_type][0], funcid=self.__event_trans[event_type][2]) #type:ignore
            self.__event_funcs.pop(event_type) #type:ignore
        elif type(event_type) == BaseEvents:
            super().remove_event(event_type) #type:ignore
        else:
            raise ValueError(f"remove_event of Button can only handle events of type BaseEvents and ButtonEvents. {type(event_type)} is not supported")
    

    @abstractmethod
    def _handle_event(self, func:Callable[...,None], event_type:BaseEvents|Any, event:Event):
        if self.object_id["state"] == "disabled" and type(event_type) != BaseEvents:
            return
        if event_type == BaseEvents.EV_MOUSE_DOWN and event_type in self.__event_funcs and self.object_id["state"] != "disabled":
            self.__ev_pressed()
        super()._handle_event(func, event_type, event_type)


#event routing functions    
    def __ev_pressed(self, event:Event):
        super()._handle_event(self.__event_funcs[ButtonEvents.EV_BTN_PRESSED],ButtonEvents.EV_BTN_PRESSED,event)

    def __ev_released(self, event:Event):
        super()._handle_event(self.__event_funcs[ButtonEvents.EV_BTN_RELEASED],ButtonEvents.EV_BTN_RELEASED,event)

    def __ev_double_pressed(self, event:Event):
        super()._handle_event(self.__event_funcs[ButtonEvents.EV_BTN_DOUBLE_PRESSED],ButtonEvents.EV_BTN_DOUBLE_PRESSED,event)