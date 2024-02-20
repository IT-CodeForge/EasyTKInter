from TGBaseWidget import TGBaseWidget
from vector2d import vector2d
from tkinter  import Message, Tk
from Framework_utils import gen_col_from_int

class TGLabel(TGBaseWidget):
    def __init__(self, myTk:Tk, txt:str="", pos_x:int=0, pos_y:int=0, width:int=80, height:int=17, fill:int=0xFFFFFF, text_col:int=0x0) -> None:
        self.__bg_col = gen_col_from_int(fill)
        self.__text_col = gen_col_from_int(text_col)
        self.object_id:Message = Message(myTk, text=txt, bg=self.__bg_col, fg=self.__text_col)
        super().__init__(vector2d(pos_x, pos_y), vector2d(width, height))
    
    @property
    def text(self)->str:
        return self.object_id.cget("text")
    
    @text.setter
    def text(self, value:str):
        self.object_id.config(text=value)
    
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
        self.text = self.text.replace(replace_str, txt)
    
    def delete_txt(self, startindex:int, endindex:int):
        self.replace_text(self.text[startindex:endindex], "")
    
    def delete_txt(self, del_str:str):
        self.replace_text(del_str, "")