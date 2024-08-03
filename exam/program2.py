"""harsha is working as a programmer in a company which process the random data and arranges into a structured format
    harshs task is to segregate the random data and obtain only characters data and process them in a meningfull way let us deduce a logic to
    help harsha in performing this operation
"""

input_string = input('Enter any string  ')

segregated_string = ''
for i in input_string:
    if( i >='a' and i<= 'z' or i >='A' and i<='Z'):
        segregated_string+=i

print(segregated_string)

    