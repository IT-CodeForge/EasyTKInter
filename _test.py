from typing import final, Final
from math import pi
from vector2d import vector2d

@final
class Test:
    TEST: Final[int] = 0

def foo(value):
    return round(value * 180 / pi, 5)

if __name__ == "__main__":
    my_vec = vector2d(1,1)
    my_vec_2 = vector2d(0,1)
    print(foo(my_vec.get_angle_to_vec(my_vec_2)))