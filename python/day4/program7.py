#pass by reference

def vararg(*user_given_list): # # receives the data into a tuple. 
    #However, if it has objects like list or dictionary, then they will received by reference only.
    user_given_list[0].remove(5)
    print(user_given_list)


number_list = [int(num) for num in input().split(',')]
vararg(number_list) # only the reference to the list is passed the actual list is not passed and actual list not modified 
print(number_list)

def function2(*num):
    num =num*2
    print(num)

num = int(input('Enter any number '))
print(num)
function2(num)
print(num)

