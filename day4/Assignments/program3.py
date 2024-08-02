
#3. Accept N strings and count the number of Palindromes in it.
user_input = [i for i in input("Enter any string  seperated by space eg  ").split()]
count =0
for i in user_input:
    if i == i[::-1]:
        count+=1
print(f'the no of palindromes in it is {count}')