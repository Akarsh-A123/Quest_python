#program to Find even placed digits in number

input_number = int(input("Enter any number to  Find even placed digits in number "))
number = [int(string) for string in str(input_number)]
for i in range(0,len(number)):
    if(i%2 ==0):
        print(number[i])