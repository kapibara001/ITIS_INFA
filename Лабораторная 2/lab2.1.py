def func(x,y):
    if -9 <= x <= -5:
        if y == -x - 7:
            return 1
    if -5 <= x <= -1 and -2 <= y <= 2:
        if (x+1)**2 + (y+2)**2 == 16:
            return 1
    if -1 <= x <= 3 and 0 <= y <= 2:
        if (x-1)**2 + (y-2)**2 == 4:
            return 1
    if 3 <= x <= 6 and 2 <= y <= 3:
        if y == 1/3*x + 1:
            return 1
    if 6 <= x <= 9 and y == 4:
        return 1
    return 0


x = float(input("Координата X: "))
y = float(input("Координата y: "))

print("Точка попадает на график" if func(x,y) else "Точка не попадает на график")