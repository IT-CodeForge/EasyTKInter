import logging
import sys
from time import perf_counter
from typing import Callable
from enum      import Enum
from TGBaseObject import TGBaseObject
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
  EV_MOUSE_DOWN  = 0
  EV_MOUSE_UP = 1
  EV_MOUSE_MOVED    = 2
  EV_KEY_PRESSED    = 3
  EV_KEY_RELEASED   = 4
  EV_CONFIGURED     = 5

class TGMainWindow(TGBaseObject,metaclass=ABCMeta):
  def __init__(self, posX:int, posY:int, width:int, height:int, title:str= "Tk"):
    if LOG: my_logger.info(f"created MainWindow with geometry: {width}x{height}+{posX}+{posY}")
    self.object_id = Tk()
    self.object_id.title(title)
    self.object_id.geometry(f"{width}x{height}+{posX}+{posY}")
    self.object_id.configure(background='#AAAAAA')
    self.object_id.protocol("WM_DELETE_WINDOW", self.appClose)
    self.__event_funcs:dict[WindowEvents,Callable[...,None]] = {}
    self.__event_trans:dict[WindowEvents, list[str|Callable[...,None]]] = {
                        WindowEvents.EV_MOUSE_DOWN:["<ButtonPress>", self.__ev_mouse_down, ""],
                        WindowEvents.EV_MOUSE_UP:["<ButtonRelease>", self.__ev_mouse_up, ""],
                        WindowEvents.EV_MOUSE_MOVED:["<Motion>", self.__ev_mouse_moved, ""],
                        WindowEvents.EV_KEY_PRESSED:["<KeyPress>", self.__ev_key_pressed, ""],
                        WindowEvents.EV_KEY_RELEASED:["<KeyRelease>", self.__ev_key_released, ""],
                        WindowEvents.EV_CONFIGURED:["<Configure>", self.__ev_configure, ""]}
   
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

  def loop_func(self):
    self.__process_func()
    end = perf_counter(self.__delta)
    self.__delta = end - self.__start
    self.__start = perf_counter()
    self.loop_func()

  def appClose(self):
    sys.exit()

  def run(self):
    self.object_id.mainloop()


#events
  def add_event(self, event_type:WindowEvents, eventhandler:Callable[...,None]):
    if LOG: logging.info(f"added event {event_type}, to MainWindow (id:{self.object_id}) event was bound to {eventhandler}")
    self.__event_funcs[event_type] = eventhandler
    self.__event_trans[event_type][2] = self.object_id.bind(self.__event_trans[event_type][0], self.__event_trans[event_type][1]) #type:ignore

  def remove_event(self, event_type:WindowEvents):
    if LOG: logging.info(f"removed event {event_type}, to MainWindow (id:{self.object_id})")
    self.object_id.unbind(self.__event_trans[event_type][0], funcid=self.__event_trans[event_type][2]) #type:ignore
    self.__event_funcs.pop(event_type)

#event routing functions  
  def __ev_mouse_down(self,event:Event):
    params = {"object_id":self.object_id,"event_type":WindowEvents.EV_MOUSE_DOWN,"event":event,"mousepos":vector2d(event.x,event.y)}
    super()._handle_event(self.__event_funcs[WindowEvents.EV_MOUSE_DOWN], params)

  def __ev_mouse_up(self,event:Event):
    params = {"object_id":self.object_id,"event_type":WindowEvents.EV_MOUSE_UP,"event":event,"mousepos":vector2d(event.x,event.y)}
    super()._handle_event(self.__event_funcs[WindowEvents.EV_MOUSE_UP], params)

  def __ev_mouse_moved(self,event:Event):
    params = {"object_id":self.object_id,"event_type":WindowEvents.EV_MOUSE_MOVED,"event":event,"mousepos":vector2d(event.x,event.y)}
    super()._handle_event(self.__event_funcs[WindowEvents.EV_MOUSE_MOVED], params)

  def __ev_key_pressed(self,event:Event):
    params = {"object_id":self.object_id,"event_type":WindowEvents.EV_KEY_PRESSED,"event":event,"char_as_str":event.char[1:-1],"char":event.keysym, "mousepos":vector2d(event.x,event.y)}
    super()._handle_event(self.__event_funcs[WindowEvents.EV_KEY_PRESSED], params)

  def __ev_key_released(self,event:Event):
    params = {"object_id":self.object_id,"event_type":WindowEvents.EV_KEY_RELEASED,"event":event,"char_as_str":event.char[1:-1],"char":event.keysym, "mousepos":vector2d(event.x,event.y)}
    super()._handle_event(self.__event_funcs[WindowEvents.EV_KEY_RELEASED], params)

  def __ev_configure(self,event:Event):
    params = {"object_id":self.object_id,"event_type":WindowEvents.EV_CONFIGURED,"event":event,"windowpos":vector2d(event.x,event.y), "width":event.width, "height":event.height}
    super()._handle_event(self.__event_funcs[WindowEvents.EV_CONFIGURED], params)