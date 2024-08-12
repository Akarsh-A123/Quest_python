'''Write a code to demonstrate use of inheritance and polymorphism using below example:
1. Eatable
1.1 Vegetarian
1.2 Non-Vegetarian

properties to be used: carbs, fat, protein, isPeelable, isBoneless

Place appropriate properties in parent class or child class and assign the values in __init__'''

class Eatable:
    def __init__(self,carbs,protien,fat):
        self.carbs 
        self.protien
        self.fat 
class Vegitarian(Eatable):
    def __init__(self,carbs,fat,protien,Peelable):
        super.__init__(carbs,protien,fat)
        self.peelable = Peelable
        print('food is vegitarian')
class Non_vegitarian(Eatable):
    def __init__(self,carbs,fat,protien,boneless):
        super.__init__(carbs,protien,fat)
        self.boneless = boneless
        print('Food is non vegitarian')