rows = (int(input("Enter the number of rows you want for your addition table: ")))

ls = []
for i in range(0, rows):
    row = []
    for j in range(0, rows):
        row.append(i+j)
    ls.append(row)
for i in range(0, rows):
    print(ls[i])

