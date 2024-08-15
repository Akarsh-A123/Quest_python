#accept the average score from the user (integer) and print the result as follows:
"""0 to 49  Fail
    50 to 74 second class
    75 to 90 first class
    91 to 100 distinction
    also check for the invalid i/p"""


Input_score = int(input('Enter the score to check the grade '))

if(Input_score >= 0 and Input_score <= 49):
    print(f'{Input_score} score result is Fail')
elif(Input_score <= 74):
    print(f'{Input_score} score result  is second class')
elif( Input_score <= 90):
    print(f'{Input_score} score result  is first class')
elif( Input_score <= 100):
    print(f'{Input_score} score result  is distinction class')
else:
    print(f'{Input_score } is invalid please enter the correct value')