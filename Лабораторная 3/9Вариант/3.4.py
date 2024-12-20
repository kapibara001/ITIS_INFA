def b_w_b(col: int):
    row = []
    for _ in range(col):
        row.append("0")
    
    for i in range(0, len(row), 4):
        row[i] = "1"
        row[i+1] = "1"

    return row

def w_b_w(col: int):
    row = []
    for _ in range(col):
        row.append("1")
    
    for i in range(0, len(row), 4):
        row[i] = "0"
        row[i+1] = "0"

    return row

clm = int(input("Введите количество столбцов: "))
rows = int(input("Введите количество строк: "))
mod_rows = rows % 4

for i in range(0, rows//2, 4):
    print(b_w_b(clm))
    print(b_w_b(clm))
    print(w_b_w(clm))
    print(w_b_w(clm))

if mod_rows == 1:
    print(b_w_b(clm))
if mod_rows == 2:
    print(b_w_b(clm))
    print(b_w_b(clm))
if mod_rows == 3:
    print(b_w_b(clm))
    print(b_w_b(clm))
    print(w_b_w(clm))