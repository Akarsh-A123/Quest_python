#check if number is perfect square
print('enter any number to check if it is perfect')
input_number = int(input())
root_number_aquare=input_number**0.5
if root_number_aquare == int(root_number_aquare):
    print(f'{input_number} is perfect square')
else:
    print(f'number is not perfect square')