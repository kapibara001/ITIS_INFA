import random

num = int(input("Количество элементов в списке: "))

arr = [random.randint(1,100) for _ in range(num)]

print(f'Изначальный список: {arr}')
print(f'Максимальный и Минимальный элемент: {max(arr)}, {min(arr)}')

minn = arr.index(min(arr))
maxx = arr.index(max(arr))

arr[minn], arr[maxx] = arr[maxx], arr[minn]
print(f'Новый список: {arr}')