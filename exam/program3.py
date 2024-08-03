"""
riya was planning to invent a game of shifting numbers.she took a aquare and placed the numbers
in each position her friend gave th logic which can be used to shift the position of given numbers.riya 
implemented that and it worked out

find the logic 


"""

row = int(input('Enter the number of row '))
col = int(input('Enter the number of columns '))

number_list = []

for i in range(row):
    column_list = []
    for j in range(col):
        column_list.append(int(input()))
    number_list.append(column_list)
print('normal list ')
for i in number_list:
    for j in i:
        print('%3s'%j,end=' ')
    print()


transposed_list =[]
for i in range(col):
    temp_list =[]
    for j in range(row):
        temp_list.append(0)
    transposed_list.append(temp_list)

for i in range(row):
    for j in range(col):
        transposed_list[i][j] = number_list[j][i]
print('transposed list ')
for i in transposed_list:
    for j in i:
        print("%3s"%j,end='')
    print()

