A = int(input("Длина стороны квадрата: "))
R = int(input("Радиус окружности: "))
x = int(input("Точка X: "))
y = int(input("Точка Y: "))

def check(x, y, A, R):
    if (x in range(-1*(A//2), (A//2)+1)) and (y in range(-1*(A//2), (A//2)+1)):
        if not (((x-(A//2))**2 + (y+(A//2))**2) <= R**2):
            return 1 
    else:
        return 0

if check(x, y, A, R):
    print("Точка принадлежит заштрихованной области")
else:
    print("Точка не принадлежит заштрихованной области")
