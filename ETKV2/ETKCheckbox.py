from .vector2d import vector2d
from .ETKBaseObject import Events
from .ETKBaseTkWidgetDisableable import ETKBaseTkWidgetDisableable
from .ETKBaseTkWidgetText import ETKBaseTkWidgetText
from tkinter import Checkbutton, IntVar, Event, Tk, EventType

class CheckboxEvents(Events):
    CB_CHECKED   = "<ButtonPress>"
    CB_UNCHECKED = "<ButtonPress>"
    CB_TOGGLED   = "<ButtonPress>"

class ETKCheckbox(ETKBaseTkWidgetDisableable, ETKBaseTkWidgetText):
    def __init__(self, tk:Tk, text:str="", pos: vector2d = vector2d(0, 0), size: vector2d = vector2d(70, 18), background_color:int=0xEEEEEE, text_color:int=0x0) -> None:
        self.__state = IntVar()
        self._tk_object: Checkbutton = Checkbutton(tk, variable=self.__state) #type:ignore
        ETKBaseTkWidgetDisableable.__init__(self, pos, size, background_color)
        ETKBaseTkWidgetText.__init__(self, text, pos, size, background_color, text_color)
        self._event_lib.update({e: [] for e in CheckboxEvents})

    @property
    def state(self) -> bool:
        return bool(self.__state.get())

    @state.setter
    def state(self, value: bool):
        self.__state.set(value)

    def _handle_tk_event(self, event: Event) -> None: #type:ignore
        match event.type:
            case EventType.ButtonPress:
                if self.enabled:
                    self._handle_event(CheckboxEvents.CB_TOGGLED, event) #type:ignore
                    if self.state:
                        self._handle_event(CheckboxEvents.CB_CHECKED, event) #type:ignore
                    else:
                        self._handle_event(CheckboxEvents.CB_UNCHECKED, event) #type:ignore
            case _:
                pass
        ETKBaseTkWidgetText._handle_tk_event(self, event) #type:ignore