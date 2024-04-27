from .ETKBaseObject import Events
from .ETKBaseTkWidgetDisableable import ETKBaseTkWidgetDisableable
from .ETKBaseTkWidgetText import ETKBaseTkWidgetText
from .vector2d     import vector2d
from tkinter      import Button, Event, Tk

class ButtonEvents(Events):
    BUTTON_PRESSED   = "<ButtonPress>"
    BUTTON_RELEASED     = "<ButtonRelease>"

class ETKButton(ETKBaseTkWidgetDisableable, ETKBaseTkWidgetText):
    def __init__(self, tk:Tk, text:str="", pos: vector2d = vector2d(0, 0), size: vector2d = vector2d(70, 18), background_color:int=0xEEEEEE, text_color:int=0x0) -> None:
        self._tk_object: Button = Button(tk, text=text) #type:ignore
        ETKBaseTkWidgetDisableable.__init__(self, pos, size, background_color)
        ETKBaseTkWidgetText.__init__(self, pos, size, background_color, text_color)
        self._event_lib.update({e: [] for e in ButtonEvents})

    @property
    def text(self)->str:
        return self._tk_object.cget("text")
    
    @text.setter
    def text(self, value:str):
        self._tk_object.config(text=value)

    def _handle_tk_event(self, event: Event) -> None: #type:ignore
        match self._TK_EVENTTYPE_TRANSLATION[event.type]:
            case "<ButtonPress>":
                if self._enabled:
                    self._handle_event(ButtonEvents.BUTTON_PRESSED, event) #type:ignore
            case _:
                pass
        return super()._handle_tk_event(event) #type:ignore