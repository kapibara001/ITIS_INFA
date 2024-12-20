import random

length = int(input('Длина массива: '))
random_array = [random.randint(1, 200) for _ in range(length)]

def find_max_two_digit_number(data_list):
    max_two_digit = None
    for i in data_list:
        if 10 <= i <= 99:
            if max_two_digit is None or i > max_two_digit:
                max_two_digit = i
                return max_two_digit

max_two_digit = find_max_two_digit_number(random_array)

print('Массив случайных чисел: ', random_array)
if max_two_digit is not None:
    print(f'Максимальное двузначное число в массиве: {max_two_digit}')
else:
    print('В массиве нет двузначных чисел')