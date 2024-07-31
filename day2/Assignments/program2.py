# program to find the largest digit in number
input_number = int(input('enter any number to find the largest digit in it '))

number_list = [int(string) for string in str(input_number)]

print(f'The largest digit  in {input_number} is {max(number_list)}')