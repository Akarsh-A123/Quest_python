#print the smallest and biggest size string in list of n strings
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
number_list = [(input('Enter the numbers ')) for i in range(Input_range)]
number_list.sort(key=(lambda e:len(e)))
print(f'the smallest size string is "{number_list[0]}" biggest size string is "{number_list[len(number_list)-1]}"')