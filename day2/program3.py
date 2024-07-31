#Find sum of the digits of number



input_number = int(input('Enter a number to find sum  of digits in it: '))
 
sum_of_digits = 0
temp_number = input_number
 
while temp_number != 0:
    reminder_digit = temp_number % 10
    temp_number = temp_number // 10
    sum_of_digits += reminder_digit
 
print(f'Number of digits in {input_number} is {sum_of_digits}')

#alter native soluion

