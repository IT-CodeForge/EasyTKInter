from typing import final, Final
from math import pi
from vector2d import vector2d

@final
class Test:
    TEST: Final[int] = 0

def foo():
    print(1)

if __name__ == "__main__":
    my_vec = vector2d(1,1)
    my_vec.rotate(pi,False)
    print(my_vec)
    my_vec.rotate(pi)
    print(my_vec)
    my_vec.normalize(False)
    print(my_vec)
    my_vec.normalize()
    print(my_vec)