from typing       import Any, Callable
from enum         import Enum
from TGBaseWidget import BaseEvents, TGBaseWidget
from vector2d     import vector2d
from tkinter      import Event, IntVar, Tk, Checkbutton

class CheckboxEvents(Enum):
    EV_CHECKED   = 0
    EV_UNCHECKED = 1
    EV_TOGGLED   = 2

class TGCheckbox(TGBaseWidget):
    def __init__(self, myTk:Tk, txt:str, posX:int, posY:int, width:int=80, height:int=17) -> None:
        self.__state = IntVar()
        self.object_id:Checkbutton = Checkbutton(myTk, text=txt, bg='#EEEEEE', fg='#000000', variable=self.__state)
        super().__init__(vector2d(posX, posY), vector2d(width, height))
        self.__event_funcs:dict[CheckboxEvents, Callable[...,None]] = {}
        self.__event_trans:dict[CheckboxEvents, list[str|Callable[...,None]]] = {
                            CheckboxEvents.EV_CHECKED:["<Button-1>", self.__event, ""],
                            CheckboxEvents.EV_UNCHECKED:["<Button-1>", self.__event, ""],
                            CheckboxEvents.EV_TOGGLED:["<Button-1>",self.__event, ""]}

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
    

#events
    def add_event(self, event_type:CheckboxEvents|BaseEvents, eventhandler:Callable[...,None]):
        if type(event_type) == CheckboxEvents:
            #special case for checkbox, since bind does not have bindings related to the state of checkbox
            if not len(self.__event_funcs):
                self.__event_trans[CheckboxEvents.EV_CHECKED][2] =  self.object_id.bind(self.__event_trans[event_type][0], self.__event_trans[event_type][1]) #type:ignore
            #
            self.__event_funcs[event_type] = eventhandler #type:ignore
        elif type(event_type) == BaseEvents:
            super().add_event(event_type, eventhandler) #type:ignore
        else:
            raise ValueError(f"add_event of Checkbox can only handle events of type BaseEvents and CheckboxEvents. {type(event_type)} is not supported")

    def remove_event(self, event_type:CheckboxEvents|BaseEvents):
        if type(event_type) == CheckboxEvents:
            self.__event_funcs.pop(event_type) #type:ignore
            if not len(self.__event_funcs):
                self.object_id.unbind(self.__event_trans[event_type][1], funcid=self.__event_trans[CheckboxEvents.EV_CHECKED][2]) #type:ignore
        elif type(event_type) == BaseEvents:
            super().remove_event(event_type) #type:ignore
        else:
           raise ValueError(f"remove_event of Checkbox can only handle events of type BaseEvents and CheckboxEvents. {type(event_type)} is not supported") 

#event routing functions       
    def __event(self, event:Event):
        checkbox_state = not self.__state.get() #needs to be inverted, since state update happens after event call
        if self.__event_funcs.get(CheckboxEvents.EV_TOGGLED, None) != None and self.object_id["state"] == "normal":
            super()._handle_event(self.__event_funcs[CheckboxEvents.EV_TOGGLED],CheckboxEvents.EV_TOGGLED,event)
        if checkbox_state and self.__event_funcs.get(CheckboxEvents.EV_CHECKED, None) != None and self.object_id["state"] == "normal":
            super()._handle_event(self.__event_funcs[CheckboxEvents.EV_CHECKED],CheckboxEvents.EV_CHECKED,event)
        if not checkbox_state and self.__event_funcs.get(CheckboxEvents.EV_UNCHECKED, None) != None and self.object_id["state"] == "normal":
            super()._handle_event(self.__event_funcs[CheckboxEvents.EV_UNCHECKED],CheckboxEvents.EV_UNCHECKED,event)