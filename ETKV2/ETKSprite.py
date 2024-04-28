from .ETKCanvas import ETKCanvas
from .ETKCanvasItem import ETKCanvasItem
from .vector2d import vector2d
from typing import Optional
import math
import json

class ETKSprite:
    def __init__(self, canvas: ETKCanvas) -> None:
        self.__canvasitem_list: list[dict[str,str | int | int | list[vector2d]]] = []
        self.__canvas: ETKCanvas = canvas
    
    @property
    def canvas(self)->Optional[ETKCanvas]:
        return self.__canvas
    
    @canvas.setter
    def canvas(self, canvas: ETKCanvas)->None:
        
        self.__canvas = canvas
    
    def __draw_sprite(self, pos: vector2d)->None:
        for canvasitemdata in self.__canvasitem_list:
            match canvasitemdata.get("type", ""):
                case "line":
                    pass

    def load_sprite(self, file_path_with_file_name: str)->None:
        pass

    def delete_sprite_data(self)->None:
        pass