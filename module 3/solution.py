#Task 1:

n=int(input("Please enter a number: "))
print(n>=100)




"""_----------------------------------------------------------_"""


#TAsk 2:
word = input("Please enter the word Spathiphyllium: ")
OutcomeupperWord = "Spathiphyllium"
lowerWord = "spathiphyllium"
upperWord = "Spathiphyllium"

if word == upperWord:
    print("Yes - Spathiphyllum is the best plant ever!")
    
elif word == lowerWord:
    print("No, I want a big Spathiphyllum!")


else:
    print("Spathiphyllum! Not", word+ "!")


"""_----------------------------------------------------------_"""





#TASK 3:
income = float(input("Enter the annual income: "))

if income <85528:
    tax=income*.18-556.02

elif income> 85528:
    tax = 14839.02+.32*(income-85528)
    
if tax <0:
    tax = 0.0

print("The tax is:", tax, "thalers")


"""_----------------------------------------------------------_"""




#TASK 4:
year = int(input("Enter a year: "))

if year%4!=0:
    print("common")
elif year%100!=0:
    print("leap")
elif year%400!=0:
    print("common")
    
else:
    print("leap")

"""_----------------------------------------------------------_"""



# TASK 5:
secret_number = 777
n = 0
while (n!=secret_number):
    n = int(input("Guess number"))
    if n!=secret_number:
        print("Ha ha! You're stuck in my loop!")
    
print("Well done, muggle! You are free now.")





"""_----------------------------------------------------------_"""

#TASk 6:

import time

for i in range(1, 6):
    print(f'{i} Missisipi')
    time.sleep(1)
    
print("Ready or not, here I come!")



"""_----------------------------------------------------------_"""




#TASK 7:
while (input):
    x=input("enter string  ")
    if x == "chupacabra":
        break




"""_----------------------------------------------------------_"""




#TASK 8: 

word_without_vowels = ""
user_word  = input("enter string : ")
user_word = user_word.upper()

for letter in user_word:
    if letter == 'A' or letter == 'E' or letter == 'I' or letter == 'O' or letter == 'U':
        continue
    print(letter)




"""_----------------------------------------------------------_"""



#TASK 9:

word_without_vowels = ""
user_word  = input("enter string : ")
user_word = user_word.upper()

for letter in user_word:
    if letter == 'A' or letter == 'E' or letter == 'I' or letter == 'O' or letter == 'U':
        continue
    else: 
        word_without_vowels += letter
print(word_without_vowels)




"""_----------------------------------------------------------_"""



#TASK 10::
blocks = int(input("Enter the number of blocks: "))
height = 0

inlayer = 1

while inlayer <= blocks:

    height += 1
    blocks -= inlayer
    inlayer += 1

print("The height of the pyramid:", height)




"""_----------------------------------------------------------_"""






#TASK 11
n = int(input("Enter a strictly positive integer: "))
steps = 0
while n != 1:
    if n % 2 == 0:
        n = n / 2
    elif n % 2 == 1: 
        n = (3*n) + 1
    steps += 1
    print(int(n))

print (f'steps count :{steps}')





"""_----------------------------------------------------------_"""





#TASK 12

hat_list = [1, 2, 3, 4, 5]  # This is an existing list of numbers hidden in the hat.

x = int(input("input integer : "))
hat_list[2] = x
hat_list.pop(4)
print(len(hat_list))
print(hat_list)