#4. Accept N strings, and check howmany of them possess the string X
user_input = [i for i in input("Enter any string  seperated by space   ").split()]
count = 0
for i in user_input:
    if 'x' in i:
        count+=1
print(f'the number of x in string is {count}')
