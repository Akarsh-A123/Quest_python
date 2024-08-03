"""
Algorithm 
get no of rows from user
get elements from user and add it to the row
starting from row one find the max element in row
store the max element in total_sum variable
store the max element in previous element variable
create a for loop starting from 1 to len(rows)
store the max value of i th row in max_element
check if the max_element is greater than previous element
if yes add max_element value to sum
    then move max_element to previous element
else stop the loop
print(total_sum)

"""

number_of_rows = int(input('Enter the number of rows'))
game_grid = []
for i in range(number_of_rows):
    columns = []
    print(f"Enter the elements for row {i}")
    for i in range(2):
        columns.append(int(input()))
    game_grid.append(columns)
print(game_grid)

total_sum = max(game_grid[i])
max_element = 0
previous_max_element = max(game_grid[i])
for i in range(1,len(game_grid)):
    max_element = max(game_grid[i])
    if max_element > previous_max_element:
        total_sum +=max_element
        previous_max_element = max_element
    else:
        break
print('The maximum possible sumof values in all the cellshe can visit is=',total_sum)
