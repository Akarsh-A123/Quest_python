class person:
    def __init__(self,age,gender,pincode):
        self.age = age
        self.gender = gender
        self.pincode = pincode


class student(person):
    def __init__(self,age,gender,pincode,residence):
        self.place = residence
        super().__init__(age,gender,pincode)     
    def details(self):
        print(f'student age {self.age} gender {self.gender} pincode {self.pincode} {self.place}')

class empyloyee(person):
    def __init__(self,age,gender,pincode,residence):
        self.place = residence
        super().__init__(age,gender,pincode)     
    def details(self):
        print(f'Employee  age {self.age} gender {self.gender} pincode {self.pincode} {self.place}')

student1 = student(20,'male',234,'hostel')
student1.details()
empyloyee1 = empyloyee(45,'female',1234,'localite')
empyloyee1.details()