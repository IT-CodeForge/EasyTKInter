from .ETKBaseTkWidget import ETKBaseTkWidget
from .vector2d     import vector2d
from tkinter      import Button, Tk
from .ETKUtils import gen_col_from_int

class ETKButton(ETKBaseTkWidget):
    def __init__(self, tk:Tk, text:str="", pos: vector2d = vector2d(0, 0), size: vector2d = vector2d(70, 18), background_color:int=0xEEEEEE, text_color:int=0x0) -> None:
        self.__text_col = gen_col_from_int(text_color)
        self._tk_object: Button = Button(tk, text=text, fg=self.__text_col) #type:ignore
        super().__init__(pos, size, background_color)

    @property
    def text(self)->str:
        return self._tk_object.cget("text")
    
    @text.setter
    def text(self, value:str):
        self._tk_object.config(text=value)