"""
1. User gives the data like this:
kerala-tiruvanantapuram karnataka-bengaluru tamilnadu-chennai
You have to separate the states and store in the list states[] and also 
the seperated capitals must be stored in capitals[]
"""

user_input = [string for string in input("Enter the state and capitals eg kerala-trivandram ").split(' ')]
state_list = []
capital_list = []
for i in user_input:
    state_list.append(i.split('-')[0])
    capital_list.append(i.split('-')[1])

print(f'the list of states equals to {state_list}')
print(f'the list of capital equals to {capital_list}')
    

    