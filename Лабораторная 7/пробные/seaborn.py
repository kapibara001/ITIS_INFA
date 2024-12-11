import пробные.seaborn as sns

df = sns.load_dataset("mpg")

# Построение графика 
# data="Имя DataFrame" x,y имена столбцов В НАБОРЕ!(НЕ ПРОИЗВОЛЬНЫЕ)!
plt1 = sns.scatterplot(data=df, x="horsepower", y="mpg")
# Задание имен осей
plt1.set(xlabel = "Horsepower", ylabel = "Miles per gallon")
# Сохранение конфига
fig1 = plt1.get_figure()
# Сохранение фото с зарешением 500 dpi
fig1.savefig('f1.png', dpi=500)