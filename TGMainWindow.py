import logging
import sys
from time import perf_counter
from typing import Callable
from enum      import Enum, auto
from TGBaseObject import TGBaseObject, BaseEvents
from tkinter   import Tk, Event
from abc       import ABCMeta, abstractmethod
from vector2d import vector2d
from TGCanvas import TGCanvas

#this is for logging purposses, if you don't want it, set "log" to False
LOG = True
if LOG:
    my_logger = logging.getLogger("MainWindow_logger")
    my_logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler = logging.FileHandler('project.log',mode='w')
    handler.setLevel(logging.DEBUG)
    handler.setFormatter(formatter)
    my_logger.addHandler(handler)
#-------------------------------------------------------------------------

class WindowEvents(Enum):
  MOUSE_MOVED    = auto()
  KEY_PRESSED    = auto()
  KEY_RELEASED   = auto()
  CONFIGURED     = auto()

class TGMainWindow(TGBaseObject,metaclass=ABCMeta):
  def __init__(self, posX:int, posY:int, width:int, height:int, title:str= "Tk"):
    if LOG: my_logger.info(f"created MainWindow with geometry: {width}x{height}+{posX}+{posY}")
    self.__window_pos = vector2d(posX, posY)
    self.__dimensions = vector2d(width, height)
    self.object_id = Tk()
    self.object_id.title(title)
    self.object_id.geometry(f"{width}x{height}+{posX}+{posY}")
    self.object_id.configure(background='#AAAAAA')
    self.object_id.protocol("WM_DELETE_WINDOW", self.app_close)
    self.canvas=TGCanvas(self.object_id, 0, 0, width, height)

    self.add_elements()


  @abstractmethod
  def add_elements(self):
    pass

  @property
  def caption(self)->str:
    return self.object_id.title()
  
  @caption.setter
  def caption(self, value:str):
    self.object_id.title(value)

  @property
  def position(self)->vector2d:
    return self.__window_pos
  
  @position.setter
  def position(self, value:vector2d):
    self.__place_window(value)
  
  @property
  def width(self)->int:
    return self.__dimensions.x
  
  @width.setter
  def width(self, value:int):
    self.__dimensions.x = value
    self.__place_window()
  
  @property
  def height(self)->int:
    return self.__dimensions.y
  
  @height.setter
  def height(self, value:int):
    self.__dimensions.y = value
    self.__place_window()
  
  def __place_window(self, pos:vector2d|None = None, dim:vector2d|None = None):
    if pos == None:
      pos = self.__window_pos
    else:
      self.__window_pos = pos
    
    if dim == None:
      dim = self.__dimensions
    else:
      self.__dimensions = dim
    
    self.object_id.geometry(f"{dim.x}x{dim.y}+{pos.x}+{pos.y}")

  def app_close(self):
    sys.exit()

  def run(self):
    self.object_id.mainloop()