#Find sum of the series:
#1 - n + n(2) - n(3) - ..... m term
input_term = int(input('Enter the term '))
sum_of_terms = 0
for i in range(0,input_term +1 ):
    term = (input_term**i)*((-1)**(i))
    sum_of_terms += term

print(f'the sum of the series is {sum_of_terms}')

