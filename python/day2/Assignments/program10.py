#print hollow square with diagonals of n lines with diagonels
input_number = int(input('Enter any no of lines '))

for i in range(1,input_number + 1):
    for j in range(1,input_number +1):
        if(i ==1 or i == input_number or j==1 or j == input_number or i == j or i+j ==6):
            print('*', end=' ')
        else:
            print(' ',end=' ')
    print()