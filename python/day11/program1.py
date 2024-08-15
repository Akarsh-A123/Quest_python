class Senior:
    def __init__(self, age, gender):
        self.age = age
        self.gender = gender
        if (self.age > 60 and self.gender == 'm') or (self.age > 45 and self.gender == 's'):
            print('15% discount on all products')

class NotSenior(Senior):
    def __init__(self, age, gender, occupation):
        super().__init__(age, gender)  
        self.occupation = occupation  
        if self.gender == 'm' and self.age < 60:
            print('100 rs discount on fast track')
        elif self.gender == 'f' and self.age < 45:
            print('100 rs discount on nika')

    def discountcheck(self):
       
        return self.age < 45 and self.occupation == 's'

class Student(NotSenior):
    def __init__(self, age, gender, occupation, stay):
        super().__init__(age, gender, occupation)  
        self.stay = stay  
        if self.discountcheck(): 
            if self.stay == 'h':
                print('500 rs discount on books and discount on groceries')
            elif self.stay == 'l':
                print('500 rs discount on books')





             
age = int(input('enter age '))
gender = input('enter gender \n m or f \n')
occupation = input('enter the occupation \n student s \n working w \n')
stay = input('enter wher you stay \n hostel h \n localite l \n')
person = Student(age,gender,occupation,stay)