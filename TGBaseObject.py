from enum import Enum, auto
from abc import abstractmethod
from tkinter import Event, EventType
import tkinter
from typing import Any, Callable
import logging

#this is for logging purposses, if you don't want it, set "log" to False
LOG = True
if LOG:
    my_logger = logging.getLogger("BaseObject_logger")
    my_logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler = logging.FileHandler('project.log',mode='w')
    handler.setLevel(logging.DEBUG)
    handler.setFormatter(formatter)
    my_logger.addHandler(handler)
#-------------------------------------------------------------------------

class BaseEvents(Enum):
    MOUSE_DOWN   = auto()
    MOUSE_UP     = auto()
    HOVERED      = auto()
    STOP_HOVERED = auto()

class TGBaseObject:
    def __init__(self) -> None:
        self.object_id
        self.object_id.bind("<ButtonPress>", self.__eventhandler)
        self.object_id.bind("<ButtonRelease>", self.__eventhandler)
        self.object_id.bind("<KeyPress>", self.__eventhandler)
        self.object_id.bind("<KeyRelease>", self.__eventhandler)
        self.object_id.bind("<Enter>", self.__eventhandler)
        self.object_id.bind("<Leave>", self.__eventhandler)
        self.object_id.bind("<Motion>", self.__eventhandler)
        self.object_id.bind("<Configure>", self.__eventhandler)
        self._event_lib:dict[str, list[dict[str, Any]]] = {
            "<ButtonPress>":[],
            "<ButtonRelease>":[],
            "<KeyPress>":[],
            "<KeyRelease>":[],
            "<Enter>":[],
            "<Leave>":[],
            "<Motion>":[],
            "<Configure>":[]
        }
        self.__type_trans = {
            EventType.KeyPress:"<KeyPress>",
            EventType.KeyRelease:"<KeyRelease>",
            EventType.ButtonPress:"<ButtonPress>",
            EventType.ButtonRelease:"<ButtonRelease>",
            EventType.Motion:"<Motion>",
            EventType.Enter:"<Enter>",
            EventType.Leave:"<Leave>",
            EventType.Configure:"<Configure>"
        }
        self.__event_trans:dict[BaseEvents, list[str|Callable[...,None]]] = {
            BaseEvents.MOUSE_DOWN:"<ButtonPress>",
            BaseEvents.MOUSE_UP:"<ButtonRelease>",
            BaseEvents.HOVERED:"<Enter>",
            BaseEvents.STOP_HOVERED:"<Leave>"
        }
        self.__event_truth_funcs = {
            BaseEvents.MOUSE_DOWN:lambda event, object_id : True,
            BaseEvents.MOUSE_UP:lambda event, object_id : True,
            BaseEvents.HOVERED:lambda event, object_id : True,
            BaseEvents.STOP_HOVERED:lambda event, object_id : True
        }
    
    def add_event(self, event_type:BaseEvents, eventhandler:Callable[...,None], sequence:str=None, truth_func:Callable[..., None]|None=None):
        if sequence == None:
            sequence = self.__event_trans[event_type]
        if truth_func == None:
            truth_func = self.__event_truth_funcs.get(event_type, lambda event, object_id : False)
        append_dict = {
            "eventhandler":eventhandler,
            "event_type": event_type,
            "truth_func": truth_func
        }
        self._event_lib[sequence].append(append_dict)

    def remove_event(self, event_type:BaseEvents, sequence:str=None):
        if sequence == None:
            sequence = self.__event_trans[event_type]
        for event in self._event_lib[self.__event_trans[event_type]]:
            if event.get("event_type") == event_type:
                self._event_lib[sequence].remove(event)
                break
        
    def __eventhandler(self, event:Event):
        for dict in self._event_lib[self.__type_trans[event.type]]:
            if dict.get("truth_func", lambda event, object_id: False)(event, self.object_id):
                try:
                    dict.get("eventhandler")(self.object_id, dict.get("event_type"), event)
                    continue
                except:
                    pass
                try:
                    params = {"object_id":self.object_id, "event_type":dict.get("event_typ"), "event":event}
                    dict.get("eventhandler")(params)
                    continue
                except:
                    pass
                try:
                    dict.get("eventhandler")()
                except:
                    ret_val = dict.get("eventhandler").__code__.co_varnames
                    raise BaseException(f"Somethings Gone Wrong, {ret_val}")
