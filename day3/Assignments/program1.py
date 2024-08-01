#accept N numbers from the user and swap the consecutive elements
"""
algorthm
1. creat a list 
2 get input from user
3 add user input  to list  using list comprehension 
4 creat a variable i =0
5 create a while loop with condition i+1 less than lenght of list
6 swap the conscutive elements 
7 increment i
6 print the list 
"""
Input_range = int(input('Enter how many numbers to input '))
number_list = [int(input('Enter the numbers ')) for i in range(Input_range)]
i =0
while i+1 < len(number_list):
    temp = number_list[i]
    number_list[i] = number_list[i+1]
    number_list[i+1] = temp
    i+=2
print(f'list with swapped conscutive elements {number_list}')
