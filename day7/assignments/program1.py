"""
two string should join with a space
two numbers will be added
string + int should be handled gracefully with exception.
"""

string_1 = input("Enter string one ")
string_2 = input("Enter string two ")
try:
    print(int(string_1) + int(string_2))
except ValueError:
    print(string_1 +" "+string_2)