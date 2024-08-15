# given list of n numbers find the no of perfect square in it
import math
number_of_customers = int(input('Enter no of coustumers '))
bill_amount_list = []
for i in range(number_of_customers):
    print(f'Enter the bill amount for coustumer_id {i}')
    bill_amount_list.append(int(input()))

count_perfect_squares = 0
for i in bill_amount_list:
    temp = math.sqrt(i)
    if(temp*temp == i):
        count_perfect_squares+=1
print(f'The no of coustomers with perfect square bill amount is ',count_perfect_squares)