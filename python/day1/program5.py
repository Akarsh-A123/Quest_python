#program to check if letter is vowel or consonant

input_letter = input('enter any letter to check if it is vowel or consonant ')
if(input_letter =='a' or input_letter =='e' or input_letter =='i' or input_letter =='u'):
    print(f'{input_letter} is a Vowel')
elif(input_letter =='A' or input_letter =='E' or input_letter =='I' or input_letter =='U'):
    print(f'{input_letter} is a Vowel')
else:
    print(f'{input_letter} is a consonant')