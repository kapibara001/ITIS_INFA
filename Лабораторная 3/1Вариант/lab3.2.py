import random

num = int(input("Количество элементов в списке: "))

arr = [random.randint(1,100) for _ in range(num)]
chet = []

for i in range(num):
    if arr[i]%2 == 0:
        chet.append(arr[i])
    else:
        continue
    
print(f'Список: {arr}')
if sum(chet) == 0:
    print("Четных не найдено.")
else:
    print(f'Максимальное четное число: {max(chet)}')
