# prin x shape mad up of stars
input_number = int(input('Enter the no of lines '))
for i in range(1,input_number +1):
    for j in range(1,input_number +1):
        if(i==j or j==input_number +1 -i):
            print('*',end=' ')
        else:
            print('',end=' ')
    print()