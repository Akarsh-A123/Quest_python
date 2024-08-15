# print pascals triangle
from math import factorial
input_number = int(input("Enter any number of lines "))
for i in range(input_number):
    for j in range(input_number - i +1):
        print(end=" ")
    for j in range(i+1):
        #ncr  = n!/((n-r)!*r!)
        print(factorial(i)//factorial(j)*factorial(i-j),end=" ")
    print()# for new line 