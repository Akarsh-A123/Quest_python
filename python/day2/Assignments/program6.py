#print fibo series of n terms with 1st 2 terms as 1 and 2
input_number = int(input('enter any number '))
a = 1
b = 2
for i in range(1,input_number+1):
    if( input_number <0):
        print('invalid input')
    else:
        if(i == 1 or i==2):
            print(i)
        else:
            c = a +b
            print(c)
            a = b
            b = c
