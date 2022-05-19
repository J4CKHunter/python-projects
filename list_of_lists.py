liste_1=[1,2,3,4]

liste_2=[[5,6],[0,9],liste_1]
print(liste_2)

liste_1.append(15)
print(liste_2)

matrix = [[1,  2,  3,  4],
          [5,  6,  7,  8],
          [9, 10, 11, 12]]
for i in range(3):
    print(matrix[i])


print([[row[i] for row in matrix] for i in range(4)])


transposed_1 = []
for i in range(4):
    transposed_1.append([row[i] for row in matrix])

print(transposed_1)


transposed = []
for i in range(4):
     # the following 3 lines implement the nested listcomp
     transposed_row = []
     for row in matrix:
         transposed_row.append(row[i])

     transposed.append(transposed_row)

print(transposed)

transpoze=[]
for i in range(4):
    transpoze_temp = []
    for j in range(3):
        transpoze_temp.append(matrix[j][i])
    transpoze.append(transpoze_temp)

for q in range(4):
    print(transpoze[q])
