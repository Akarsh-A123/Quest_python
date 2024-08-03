'''
algorithm
get original string from user
get rotated string from user
now concatinate rotated_string + rotated_string
now check if original string is presented in concatinated string using find method
if present print yes


'''
original_str = input('Enter the original string: ')
rotated_str = input('Enter the rotated string: ')
 
temp_str = rotated_str * 2
if temp_str.find(original_str) != -1:
    print(f'{rotated_str} is rotated string of {original_str}')
else:
    print(f'{rotated_str} is Not rotated string of {original_str}')