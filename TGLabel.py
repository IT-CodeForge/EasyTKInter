from TGBaseWidget import TGBaseWidget
from vector2d import vector2d
from tkinter  import Label, Tk

class TGLabel(TGBaseWidget):
    def __init__(self, myTk:Tk, txt:str, posX:int, posY:int, width:int=80, height:int=17) -> None:
        self.object_id:Label = Label(myTk, text=txt, bg='#FFFFFF', fg='#000000')
        super().__init__(vector2d(posX, posY), vector2d(width, height))
    
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