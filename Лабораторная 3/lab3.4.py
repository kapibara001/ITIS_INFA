import random
    
rows = 5 # количество строк...
cols = 4 # количество столбцов
    
array=[[random.randint(0,100) for _ in range(cols)] for _ in range(rows)]
    
for row in array:
    print(row)

maxEven=0

for i in range(len(array)):
    for j in range(len(array[i])):
        #if array[i][j]%2==0 and maxEven< array[i][j]:
        if array[i][j]%2==0 and maxEven< array[i][j] and i == j: # Задание после выполнения базы
            maxEven = array[i][j]

print(maxEven)
