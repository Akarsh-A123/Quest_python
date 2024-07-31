# program to find the second largest digit in number
input_number = int(input('enter any number to find the largest digit in it '))

number_list = [int(string) for string in str(input_number)]
number_list.sort()
list_length = len(number_list) 
print(list_length)
print(f'The largest digit  in {input_number} is {number_list[list_length -2 ]}')