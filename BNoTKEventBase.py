from typing import Callable

class BNoTKEventBase:
    def __init__(self) -> None:
        self._event_lib:dict[str,list] = {}

    def add_event(self, event_type, eventhandler:Callable[...,None], sequence:str=None):
        if event_type not in self._event_lib:
            self._event_lib[event_type] = []
        self._event_lib[event_type].append(eventhandler)

    def remove_event(self, event_type, eventhandler:Callable[..., None], sequence:str=None):
        self._event_lib
        
    def _eventhandler(self, event_type):
        if event_type not in self._event_lib.keys():
            return
        for eventhandler in self._event_lib[event_type]:
            try:
                eventhandler()
            except:
                pass