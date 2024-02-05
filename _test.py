from typing import final, Final
from math import pi
from vector2d import vector2d

@final
class Test:
    TEST: Final[int] = 0

def foo(value):
    return round(value * 180 / pi, 5)

if __name__ == "__main__":
    temp = {1:"hi", 2:"hallo"}
    if 1 in temp:
        print(1)
    if "hi" in temp:
        print(2)