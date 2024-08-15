"""
5. Accept N main strings and N sub strings into lists and check create a list of numbers of 0s and 1s where 0 represents that the sub string at respective index is not a substring of the main string.
 
main_list = ['andhra pradesh', 'kerala', 'maharashtra', 'haryana']
sub_list  = ['pradesh', 'south', 'rashtra', 'punjab']
 
presence = [1, 0, 1, 0]
"""
main_list = [i for i in input("Enter any string  seperated by space   ").split(",")]
sub_list = [i for i in input("Enter any string  seperated by space   ").split(",")]
presence_list = []
for i in main_list:
    for j in sub_list:
      flag = False
      k = i.find(j)
      if(k >= 0):
         flag = True
         break
      else:
         flag = False
    if(flag):
       presence_list.append(1)
    else:
       presence_list.append(0)
print(presence_list)