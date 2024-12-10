import pandas as pd

data = {
    'specials': ["Adelie", "Adelie", "Chinstrap", "Gentoo", "Gentoo"],
    'island': ["Dream", "Torgensenm", "Biscoe", "Torgensenm", "Biscoe"],
    'body_mass': [5400, 3200, 4100, 5300, 4850],
    'gender': ["Male", "Female", "Male", "Male", "Female"],
    }

df = pd.DataFrame(data)
print(df)
print("\n")

# Изменение 1 элемента в столбце 'body_mass' в 1.2 раза
df.loc[0, 'body_mass'] *= 1.2
print(df)
print("\n")

# Изменение столбца 'body_mass' в 1.2 раза
df['body_mass'] *= 1.2
print(df)
print("\n")

# Имена столбцов. list - для нормального отображение в строке вывода 
print(list(df.columns))
print("\n")

# Создание таблицы из таблицы df, где присутсвуют только те строки, стоблцы которых носят название "Adelie"
df1 = df[df.specials == "Adelie"]
print(df1)
print("\n")

# Создание таблицы из таблицы df, где присутсвуют только те строки, в которых значение в столбце "body_mass" более 6000
df2 = df[df.body_mass > 6000]
print(df2)
print("\n")

# Несколько условий
df3 = df[df.body_mass > 6000][df.specials == "Adelie"]
print(df3)
print("\n")

df.loc[df.body_mass > 6000, "body_mass"] *= 2
print(df)
print("\n")

#--------------------------------------------------------------

