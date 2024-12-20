numbers1 = []
numbers2 = []
ob = []

num = int(input("Чисел в списке 1 будет: "))
for i in range(num):
    n = int(input("Добавляем в список 1 число: "))
    numbers1.append(n)

num = int(input("Чисел в списке 2 будет: "))
for i in range(num):
    n = int(input("Добавляем в список 2 число: "))
    numbers2.append(n)

if len(numbers1) > len(numbers2):
    for i in range(len(numbers1)):
        if numbers1[i] in numbers2:
            ob.append(numbers1[i])
else:
    for i in range(len(numbers2)):
        if numbers2[i] in numbers1:
            ob.append(numbers2[i])

print(f'Общие числа в списках: {set(ob)}')