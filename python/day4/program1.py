# find the n th term in the series 1 2 2 3 3 5 5 7 8
#her the series is combination of fib series and prime number series 
# fib series are in odd index and prime series are in even index
# if term is odd print n//2 +1 th fibo term 
# if term is even print n/2 the prime term
import math
#function to find nth fibo number
def find_fib_term(n):
    thrid_number = 0
    first_number  = 1
    second_number = 2  
    if n == 1:
        thrid_number = 1
    elif n == 2:
        thrid_number = 2
    else:
        thrid_number  = 0
        count = 2
        while count <= n:
            thrid_number = first_number + second_number
            count += 1
            if count == n:
                return thrid_number
            first_number = second_number
            second_number = thrid_number
    return thrid_number
#function to find prime number
def find_prime(num):
    for i in range(2, math.ceil(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True

input_number = int(input('Enter the n th term '))
if(input_number % 2 ==0):
    j = 0
    if input_number == 1:
        j = 2
    elif input_number == 2:
        j = 3
    else:
        count = 2
        j = 4 #Number in J is checked if Prime or not
        while count <= input_number/2:
            if find_prime(j):
                count += 1
            if count == input_number/2:
                break
            j += 1
    print(f'the {input_number} nth number in series is  {j}')
else:
    temp_number = input_number//2 + 1
    print(f'the {input_number} nth  number in series is {find_fib_term(temp_number)}')
    