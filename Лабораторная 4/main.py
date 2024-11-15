import re


#Получает на вход текстовый документ
text = str(input("Моя строка: "))
#text = "Люблю прогить на питоне! #coding #python #coding #nice #coding #python #python #python #python #coding #coding #coding" 
print(f'Текст: {text}')
list_hes = re.findall(r"#\w+", text)


#Находит все хеш-теги
print("Хештеги в тексте: ")
for i in list_hes:
    print(i)


#Выводит список всех хеш-тегов без повторений
new_list = set(list_hes)
print("\nСписок хеш-тегов без повторов: ")
for i in new_list:
    print(i)
    

#Подсчитывает, сколько раз каждый хет-штег встречается в строке
ch_num = []
ch_hash = []

need = list(new_list)
print("\nЧастота встречаемости хеш-тегов:")
for i in range(len(need)):
    print(f'{need[i]} - {text.count(need[i])} раз')
    ch_num.append(text.count(need[i]))
    ch_hash.append(need[i])


#Сортирует хеш-теги по частоте встречаемости в порядке убывания
print("\nСортировка по количеству хеш-тегов в строке(в порядке убывания): ")
#print(ch_hash, list(reversed(sorted(ch_num))))
new_spis = []
for i in range(len(ch_num)):
    new_spis.append(ch_hash[i]) 
    new_spis.append(ch_num[i])

for i in range(len(ch_hash)):
    max_kol = ch_num.index(max(ch_num))
    print(f'Хеш-тег {ch_hash[max_kol]} - {ch_num[max_kol]} раз')
    ch_num.remove(ch_num[max_kol])
    ch_hash.remove(ch_hash[max_kol])