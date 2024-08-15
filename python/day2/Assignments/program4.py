# check if number is prime
input_number = int(input('Enter any number to check prime or not '))
flag = False

if(input_number == 1):
    print('number is not prime')
elif input_number > 1:
    for i in range(2,input_number):
        if(input_number % i == 0):
            flag =True
            print('not prime')
            break
        

if(flag):
    print(f'{input_number} is not prime')
else:
    print('number is prime')