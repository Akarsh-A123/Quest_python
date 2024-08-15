#List comprhension
squar1 = []
for i in range(10):
    squar1.append(i*i)
print('squares1 =',squar1)
#--------------------------
"""List Comprehension
[x**2 for x in range(10)]
 
step1: [ ]
We are saying, we need a list
 
step2: x ** 2
elements of the list will be x ** 2
 
step3: for x in range(10)
values for x will be supplied from the for loop"""
#-----------------------------
squares2 = [x**2 for x in range(10)]
print('Squares2 = ', squares2)
#--------------------------------------
#Using Map and Lambda Function:
 
squares3 = list(map(lambda x: x**2, range(10)))
#map function collects all the values gengerated by lambda fn and passes to list 
print('Squares3 = ', squares3)
#--------------
input_numbers = list(map(int, input().split()))
 
"""
    map() function returns a map object(which is an iterator) of the results after applying the given function to each item of a given iterable (list, tuple etc.)
step1: input()
Read a string
 
step2: input().split()
The string read by input() is split on spaces, because default delimiter(argument) of split is space
 
input.split('@') # The delimiter here is '@'
12@1@124@34@57
'12', '1', '124', '34', '57'
 
delimiter: The character that seperates 2 values
 
step4:
map(int, input().split())
The many strings after applying split() on the input string is passed one by one to map()
The map() is converting all the values (strings) into int and later all these int values we are using to create a list."""