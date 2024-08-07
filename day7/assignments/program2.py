
"""* Name

* Age
 
15% discount for all product for senior citizen
 
* Gender

male senior citizen (60 and above)

female senior citizen (45 and above)
 
100 rupees nyka, fastrack, if female (<45)

100 coupon on titan, fastrack, if male (<60)

----
 
*Occupation: Working, Student (PIN code should be local)
 
College: 500 coupon on books

Working: NA
 
----

*Residence: Hosteller, Localite (Hostel name should be valid)
 
Hosteller: Groceries

Localite: NA
 
----

* Armed Forces: Yes/No (Check from external file)
 
Yes: Free pass for R-day parade for 2"""


 
age = int(input("Enter age: "))
gender = input("Enter gender: \nM. Male\nF. Female.")
occupation = input("Enter occupation :\n s student \n w working  ")
stay = input('Enter stay location : \n l locality \n h hostel ')







if age >=60 and gender == 'm':
    print('15 % discount on all products ')
elif age >= 45 and gender == 'f':
        print('15 % discount on all products ')
elif (age < 60 and age >= 45)  and gender == 'm':
     print('100 rs fast track discount')
elif age < 45 and gender == 'm':
    print('100 rs fast track discount ')
    if occupation == 's' and stay=='h' :
            print('500 rs discount on books and discount on grocerries ')
    elif occupation == 's' and stay =='l':
          print('500 rs discount on books')
elif(age < 45 and gender =='f'):
     print('100 rs discount on nika ')
     if occupation == 's' and stay =='h':
          print('500 rs discount on books and discount on groceries')
     elif occupation =='s' and stay =='l':
          print('500 rs discount on books ')
        




