#count the number of prime digits in a number
input_number = int(input('Enter any number to check prime or not '))
temp_number = input_number
count = 0
while(temp_number > 0):
    reminder = temp_number %10
    temp_number = temp_number // 10
    if(reminder != 1):
        if(reminder == 2):
            count +=1
        else:
            flag = False
            for i in range(2,reminder):
                if(reminder % i == 0):
                    flag = True
                    break
            if(flag == False):
                count +=1


print(f'the number of prime digits in {input_number} is {count}')