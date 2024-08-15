#get n numbers from user and find biggest and samallest and biggest nnumber

number_range = int(input('Enter how many numbers is required'))
print('Enter numbers')
array = [] 
for i in range(number_range):
    array.append(int(input()))

print('Array = ',array)
smallest_number = array[0]
biggest_number = array[0]
for i in range(1,number_range): #the range starts from 1 because we assumed small and big array is at index[0] and we start comparison from index 2
    if array[i] < smallest_number:
        smallest_number = array[i]
    if array[i] > biggest_number:
        biggest_number = array[i]
print(f'the biggest number in array is {biggest_number}')
print(f'the smallest number in array is {smallest_number}')