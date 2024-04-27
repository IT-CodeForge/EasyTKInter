from tkinter import Tk
from typing import Callable

class ETKTimer:
    def __init__(self, tk: Tk, interval_in_ms: int, timer_function:Callable[[], None])->None:
        self.__my_Tk: Tk = tk
        self.__timer_function: Callable[[], None] = timer_function
        self.interval_in_ms: int = interval_in_ms
        self.__is_running = True
        self.__my_Tk.after(self.interval_in_ms, self.trigger)
    
    @property
    def is_running(self)->bool:
        return self.__is_running
    
    @is_running.setter
    def is_running(self, value: bool)->None:
        self.__is_running = value
        if value:
            self.trigger()
    
    def trigger(self)->None:
        self.__timer_function()
        if self.__is_running:
            self.__my_Tk.after(self.interval_in_ms, self.trigger)