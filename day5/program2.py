#creat a 2d (matrix ) array

rows = int(input("Enter no of row of the matrix1"))
columns = int(input("Enter no of columns of the matrix1"))
matrix1 = []
for i in range(rows):
    print(f"Enter {columns} numbers for row {i+1} ")
    row_numbers = []
    for j in range(columns):
        row_numbers.append(int(input()))
    matrix1.append(row_numbers)


####################################
rows2 = int(input("Enter no of row of the matrix2"))
columns2 = int(input("Enter no of columns of the matrix2"))
matrix2 = []
for i in range(rows2):
    print(f"Enter {columns2} numbers for row {i+1} ")
    row_numbers = []
    for j in range(columns):
        row_numbers.append(int(input()))
    matrix2.append(row_numbers)

print('matrix1')
for i in matrix1:
    for j in i:
        print('%3s'%j,end='')
    print()

print('matrix2')
for i in matrix2:
    for j in i:
        print('%3s'%j,end='')
    print()
 ###################################
sum_matrix = []
if(rows==rows2 and columns==columns2):
    
    for i in range(rows):
        row_numbers = []
        for j in range(columns):
            row_numbers.append(matrix1[i][j] + matrix2[i][j])
        sum_matrix.append(row_numbers)

print('sumed matrix is ')
for i in sum_matrix:
    for j in i:
        print('%3s'%j,end='')
    print()
