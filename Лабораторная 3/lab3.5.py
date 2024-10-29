import random

def edin(quantity):
    row = [1 for _ in range(quantity)]
    return row

def edin_zero(quantity):
    row = [0 for _ in range(quantity-1)]
    row.insert(0, 1)
    return row 

def zero_edin(quantity):
    row = [0 for _ in range(quantity-1)]
    row.insert(quantity, 1)
    return row 

rows = int(input("Количество строк: "))
clmns = int(input("Количество стобцов: "))

#array = [[random.randint(1,20) for _ in range(clmns)] for _ in range(rows)]

for i in range(1, rows+1):
    if i%2 != 0:
        print(edin(clmns))
    if i%2==0 and i%4!=0:
        print(zero_edin(clmns))
    if i%4==0:
        print(edin_zero(clmns))