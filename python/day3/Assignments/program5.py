#demonstrate different ways to add elements and delet elements from list
#add elements to list 
Input_range = int(input('Enter how many numbers to elements '))
# for loop method
number_list1 = []
for i in range(5):
    (input('Enter the element ')) 
    number_list1.append(i)
print(f'list 1',number_list1)

# list comprehension method
number_list2 = [int(input('Enter the element ')) for i in range(Input_range)]
print(f'list 2 {number_list2}')

#extend method
number_list3 = [1,2,3]
new_elements = [4,5,6]
number_list3.extend(new_elements)
print(f'list 3 {number_list3}')

#methods to remove elemnts form list
# remove method
number_list4 = [1,2,3,4,5]
number_list4.remove(3)
print(f'list 4 after removing 3 from list {number_list4}')
# pop method
number_list5 = [1,2,3,4,5]
number_list5.pop(1)
print(f'list 5 after removing an element  from index 2 of  list {number_list5}')


