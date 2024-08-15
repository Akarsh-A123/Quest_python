#3d matrix
def generatematrix(rows,columns):

    matrix1 = []
    for i in range(rows):
        print(f"Enter {columns} numbers for row {i+1} ")
        row_numbers = []
        for j in range(columns):
            row_numbers.append(int(input()))
        matrix1.append(row_numbers)
    return matrix1
matrices = int(input('enter no of matrix for 3d matrix'))
row = int(input('enter no of rows'))
col = int(input('enter no of columns'))

matrix_3d = []
for i in range(matrices):
    matrix_3d.append(generatematrix(row,col))
print(matrix_3d)

for i in matrix_3d:
    for j in i:
        print('%3s'%j,end='') 

