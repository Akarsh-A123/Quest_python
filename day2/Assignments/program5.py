# print equilateral triangle
input_number = int(input('Enter the number of lines '))
number = input_number
for i in range(1,input_number+1):
    print(' '*number, end='')
    print('*'*i,)
    number-=1