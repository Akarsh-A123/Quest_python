"""
* Name
* Branch: ECE  					
* Preference: Maths, Art
--
* Maths: 80
* English: 96
* Art: 97

pass marks is 35

Marketing (ECE): Art>90 + Literature>90, pass in all subject (maths > 35) prefrence(art)

Accounts (BCOM): Maths>95, pass in all subject (English and Arts > 35) prefrence(maths)

Sales (MECH): Maths>90 + Literature>90, pass in all subject (Art > 35) prefrence(maths)
"""

try:
    while True:
        name = str(input('Enter your name '))
        branch = int(input('Enter Branch \n EcE 1 \n Mech  2 \n Bcome  3  '))
        if (branch != 1) and (branch != 2) and (branch != 3):
            print('invalid input enter correct branch ')
            continue
        preference_list = [ int(i) for i in input("enter your preference if more than one seperate by ',' \n maths 1 \n art 2  ").split(',')]
        print(preference_list)
        if len(preference_list) > 2 or len(preference_list) < 1:
            print('Invalid input enter correct preference ')
            continue
        elif (1 not in preference_list) and (2 not in preference_list) :
            print('Invalid input enter correct preference list ')
            continue
        marklist = [int(i) for i in input("Enter marks for maths ,english,art ").split(',')]
        if len(marklist) != 3:
            print('invalid input enter correct mark list ')
            continue
        print('all input correct')
        break
        #print(marklist)
except:
    print('invalid input')
#mark_list  [maths ,english ,art ]
# branch ece-1,mech-2 , bcom -3
# preference list [1- maths, 2-art]  

if branch == 1:
    if 2 in preference_list:
        if marklist[0] > 35 and marklist[2] >90 and marklist[1] >90:
            print("You are selected for Marketting")
        else:
            print("Your marks do not qualify")
    else:
        print('preference list do not match')
elif branch == 3:
    if 1 in preference_list:
        if marklist[0] > 95 and marklist[2] >35 and marklist[1] > 35:
            print("You are selected for Accounts")
        else:
            print("Your marks do not qualify")
    else:
        print('your prefrence does not match ')
elif branch == 2:
    if 1 in preference_list:
        if marklist[0] > 90 and marklist[2] >90 and marklist[1] > 35:
            print("You are selected for Sales")
        else:
            print("Your marks do not qualify")
    else:
        print('preference do not qualify ')
