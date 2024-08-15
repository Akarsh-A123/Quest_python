#find smallest and biggest elements in a list of n numbers
"""
algorthm
1. creat a list 
2 get input from user
3 add user input  to list  using list comprehension 
4 sort the list using list method
5 print element in index 0 that is smallest element
6 print element in last index that is largest element 
"""
Input_range = int(input('Enter how many numbers to elements '))
number_list = [int(input('Enter the numbers ')) for i in range(Input_range)]
number_list.sort()
print(f'the largest number in the list is {number_list[len(number_list)-1]} and  smallest number in list is {number_list[0]}')
