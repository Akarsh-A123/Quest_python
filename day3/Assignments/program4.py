#remove negative numbers from list of n numbers
"""
algorthm
1. creat a list 
2 get input from user
3 add user input  to list  using list comprehension 
4 create an empty list 
5 creat for loop and itterate through list
6 check if number is greater than or equal to zero
7 if true append the number to new list 
"""
Input_range = int(input('Enter how many numbers to elements '))
number_list = [int(input('Enter the number ')) for i in range(Input_range)]
new_list = []
for i in number_list:
    if(i >= 0):
        new_list.append(i)
    

print(new_list)