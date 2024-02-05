from abc import abstractmethod
from utilities import inspect_type #type:ignore
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

class TGBaseObject:
    def __is_class_method(self, func: Callable[..., None]):
        method_type = inspect_type(func) #type:ignore
        if method_type in ["function","staticmethod"]:
            return False
        else:
            return True
    
    def _handle_event(self, func: Callable[..., None], paramdict:dict[str, Any]={}):
        print(paramdict)
        event_type = paramdict.get("event_type", "ERROR:event_type not found")
        my_id = paramdict.get("object_id", "ERROR:object_id not found")
        if LOG: logging.info(f"handled event {event_type}, from widget with id: {my_id}")
        std_arg_len = self.__is_class_method(func)
        if func.__code__.co_argcount == std_arg_len:
            func()
        elif func.__code__.co_argcount == std_arg_len + 1:
            func(paramdict)
        else:
            raise BaseException(f"the event method can only have one parameter in addition to the class. The given function {func.__name__} has {func.__code__.co_argcount - std_arg_len} parameters to many, parameter list: {func.__code__.co_varnames}")
