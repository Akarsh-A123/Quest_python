'''
2. Accpet a string of space seperated numbers and store them as a matrix (list of lists) of n rows.
Now print the matrix row-wise
'''
user_input = [i for i in input("Enter any numbers seperated by space eg '1 2 3' ").split()]
rowcount_input = int(input('Enter the no of rows '))
new_list = []
end_index = rowcount_input
start_index = 0
for i in range(rowcount_input):
    new_list.append(user_input[start_index:end_index])
    start_index = end_index
    end_index = end_index*2
print(new_list)