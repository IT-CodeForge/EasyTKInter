from vector2d import vector2d
from random   import randint
from time     import perf_counter

times = []
sol_list = []
vec_a = vector2d()
vec_b = vector2d()
vec_1 = vector2d()
vec_2 = vector2d()   

if __name__ == "__main__":
    for i in range(int(150/4*150/4)+1):
        vec_a = vector2d(randint(-500,500),randint(-500,500))
        vec_b = vector2d(randint(-500,500),randint(-500,500))
        vec_1 = vector2d(randint(-500,500),randint(-500,500))
        vec_2 = vector2d(randint(-500,500),randint(-500,500))
        start = perf_counter()
        st1 = vec_a
        st2 = vec_1
        sp1 = vec_b - vec_a
        sp2 = vec_2 - vec_1
        try:
            a = ((st1.y-st2.y)*sp2.x-(st1.x-st2.x)*sp2.y)/(sp1.x*sp2.x-sp1.y*sp2.y)
            if a > 0 and a < 1:
                sol_list.append([sp1,sp2])
            print("hi")
        except:
            pass
        end = perf_counter()
        times.append(end-start)
    print(sum(times)/len(times))