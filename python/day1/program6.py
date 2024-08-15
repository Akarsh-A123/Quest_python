#program to check is number is single digit or not
input_number = int(input('Enter any number to check if it is single digit or not '))
if(input_number/10 >= 1):
    print(f'{input_number} is not single digit')
else:
    print(f'{input_number} is single digit ')