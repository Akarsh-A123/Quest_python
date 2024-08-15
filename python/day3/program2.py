#check if it is prime number
#a number is prime if its not  divisible only by 2 factors its self and 1
# if a number is not divisable upto number/2 then number is prime number
# if a number is not divisable upto ceal(sqrt(number)) then its prime number
import math
input_number = int(input('Enter any number to check if its prime or not '))
flag = False
if(input_number > 1):
    for i in range(2,math.ceil(math.sqrt(input_number))):
        if(input_number % i == 0):
            flag = True
            break
else:
    print('number is not prime number')
if(flag):
    print('The number is not prime number')
else:
    print('number is prime number')
