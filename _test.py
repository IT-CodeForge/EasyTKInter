from math import pi
from vector2d import vector2d

class Test:
    def __init__(self) -> None:
        self.my_list = [1, 2]
        print("Test" ,self.my_list)

class Test1(Test):
    TEST = 0
    def __init__(self) -> None:
        super().__init__()

    def foo(self):
        self.my_list = [2,3]
        print("Test 1",self.my_list)

class Test2(Test):
    def __init__(self) -> None:
        super().__init__()
    
    def foo(self):
        print("Test 2",self.my_list)

def foo(value):
    value()

if __name__ == "__main__":
    temp1 = Test1()
    temp2 = Test2()
    temp1.foo()
    temp2.foo()