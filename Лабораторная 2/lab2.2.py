import math

def func(R1, R2, x, y):
    my_r = math.sqrt(x**2 + y**2)
    if  R1 <= my_r <= R2:
        return 1
    return 0


R1 = float(input("Радиус 1: "))
R2 = float(input("Радиус 2: "))
x = float(input("X: "))
y = float(input("Y: "))

print("Входит в область" if func(R1, R2, x, y) else "Не входит")