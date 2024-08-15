class data:
    def __init__(self,age,occupation,stay,gender):
        self.age = age
        self.occupation = occupation
        self.stay = stay
        if age > 60  and gender == 'm' or age > 45 and gender =='f':
            return True
        else:
            return False
class senior(data):
    if data == True:
        print('15 % discount on all products ')
class junior(data):
    if data == False:
        if gender == 'm':
            print('100 rs discount on fast track')
        elif gender =='f':
            print('100 rs discount nika ') 
class female(data):
    def discountcheck(self):
        if self.age >=45:
            print('15 % discount on all products')
        elif self.age < 45:
            print('100 rs discount on nika')
            if self.occupation == 's' and self.stay =='h':
                print('500 rs discount on books and discount on grocerries')
            elif self.occupation == 's' and self.stay =='l':
                print('500 rs discount on books')
class male(data):
    def discountcheck(self):
        if self.age >=60:
            print('15 % discount on all products ')
        elif self.age < 60 and self.age >=45:
            print('100 rs fast track discount')
        elif self.age < 45:
            print('100 rs off on fast track discount')
            if self.occupation == 's' and self.stay =='h':
                print('500 rs discount on books and discount on groceries')
            elif self.occupation =='s' and self.stay =='l':
                print('500 rs discount on books ')

age = int(input("Enter age: "))
gender = input("Enter gender: \nm. Male\nf. Female.")
occupation = input("Enter occupation :\n s student \n w working  ")
stay = input('Enter stay location : \n l locality \n h hostel ')

if gender =='m':
    male1 = male(age,occupation,stay)
    male1.discountcheck()
elif gender =='f':
    female1 = female(age,occupation,stay)
    female1.discountcheck()
else:
    print('Enter valid details')
