#TASK 2 : 
zero = '###\n# #\n# #\n# #\n###\n\n'
one = '#\n#\n#\n#\n#\n\n'
two = '###\n  #\n###\n#  \n###\n\n'
three = '###\n  #\n###\n  #\n###\n\n'
four = '# #\n# #\n###\n  #\n  #\n\n'
five = '###\n#  \n###\n  #\n###\n\n'
six = '###\n#  \n###\n# #\n###\n\n'
seven = '###\n  #\n  #\n  #\n  #\n\n'
eight = '###\n# #\n###\n# #\n###\n\n'
nine = '###\n# #\n###\n  #\n###\n\n'

def seven_segment_display(digit):
    if digit >= 0:
        digit = str(digit)
        digit_list = list(digit)
        new_digit = ''
        for i in range(len(digit_list)):
            if digit_list[i] == '0':
                new_digit += zero
            if digit_list[i] == '1':
                new_digit += one
            if digit_list[i] == '2':
                new_digit += two
            if digit_list[i] == '3':
                new_digit += three
            if digit_list[i] == '4':
                new_digit += four
            if digit_list[i] == '5':
                new_digit += five
            if digit_list[i] == '6':
                new_digit += six
            if digit_list[i] == '7':
                new_digit += seven
            if digit_list[i] == '8':
                new_digit += eight
            if digit_list[i] == '9':
                new_digit += nine
    return new_digit
print(seven_segment_display(123))






#TASK 3 : 

def encrypt(text,s):
	result = ""
	for i in range(len(text)):
		char = text[i]

		# Encrypt uppercase characters
		if (char.isupper()):
			result += chr((ord(char) + s-65) % 26 + 65)

		# Encrypt lowercase characters
		else:
			result += chr((ord(char) + s - 97) % 26 + 97)

	return result

text = input("enter string")
s = int(input("enter integer"))
print ("Text : " + text)
print ("Shift : " + str(s))
print ("Cipher: " + encrypt(text,s))





#TASK 4: Palinrome algorithm:


def isPalindrome(s):
	return s == s[::-1]

s = input("input string")
ans = isPalindrome(s)

if ans:
	print("Yes its a palindrome ")
else:
	print("No")

#TASK 5: Anagram algorithm:
def check(s1, s2):
	if(sorted(s1)== sorted(s2)):
		print("The strings are anagrams.")
	else:
		print("The strings aren't anagrams.")		
		
s1 =input("enter firts anagram")
s2 =input("second wor")
check(s1, s2)


#TASK 6: date of life:

test_str = str(input("enter date of strings"))
print("The original string is : " + str(test_str))

res = 0
for num in test_str:
	res += int(num)
	if res > 9:
		res = res % 10 + res // 10

print("Life Path Number : " + str(res))

#TASK 7 find a word : 

def isSubSequence(string1, string2, m, n):
	if m == 0:
		return True
	if n == 0:
		return False
	if string1[m-1] == string2[n-1]:
		return isSubSequence(string1, string2, m-1, n-1)
	return isSubSequence(string1, string2, m, n-1)

string1 = "donut"
string2 = "Nabucodonosor"

if isSubSequence(string1, string2, len(string1), len(string2)):
	print ("Yes")
else:
	print ("No")