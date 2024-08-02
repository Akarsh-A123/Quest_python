number = [1,2]
#insert element at end of the list
number[len(number):] = [3] #we can add only range of values 
print(number)
###############
number.append(4)
print(number)
################
number.insert(len(number),5)
print(number)
number.insert(-1,'hai')
print(number)

##########
#delete number from list
del number[1:3]
print(number)
del number[2]
print(number)
del number[:]
print(number)


