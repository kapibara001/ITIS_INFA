import pandas as pd

data = {
    'specials': ["Adelie", 'Adelie', 'Chinstrap', 'Gentoo', 'Gentoo'],
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


