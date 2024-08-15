"""

Assignment:
Accept a string of Pairs of Peranthesis and check if they are arranged properly. If so, print the number of pairs of peranthesis else print improper arrangement.
 
((()())) : 4 pairs
(()))	 : improper arrangement
"""
import pdb
pdb.set_trace() # to run code in debugger 
def count_paranthesis(parenthesis):
    count_1 =0
    count_2=0
    for i in parenthesis:
        if i =='(':
            count_1 +=1
        elif i ==')':
            count_2+=1
    if(count_1==count_2):
        i=0
        length = len(parenthesis)
        flag = True
        while i+1 <len(length):
            if(parenthesis[i] == parenthesis[length-i-1]):
                flag =True
            else:
                flag =False
        if(flag ==False):
            print(f"no of pairs is {count_1}")
        else:
            print("improper arrangement ")