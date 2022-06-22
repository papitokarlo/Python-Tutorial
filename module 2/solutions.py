#TASK 1 :
print("Programming","Essentials","in", sep="***", end="...")

print("Python\n", sep="", end="")




"""_----------------------------------------------------------_"""


#TASK 3 :
print('"I\'m"\n"\"learning"\"\n"\"\"Python"\"\"')




"""_----------------------------------------------------------_"""


#TASK 4 : 

john=0
mary=0
adam=0

john=3
mary=5
adam=6

print("John: ",john,"Mary: ",mary,"Adam: ",adam)
totalApples=john+mary+adam

print(totalApples)

uiru=298
newTotal=totalApples+uiru 
print("The total Apples is", totalApples,"but with new variable uiru is ", newTotal)
print("The total Apples in the story is", totalApples)




"""_----------------------------------------------------------_"""

#TASK 5 :

kilometers = 12.25
miles = 7.38

miles_to_kilometers = miles*1.61
kilometers_to_miles = kilometers/1.61

print(miles, "miles is", round(miles_to_kilometers, 2), "kilometers")
print(kilometers, "kilometers is", round(kilometers_to_miles, 2), "miles")


"""_----------------------------------------------------------_"""




#TASK 6:

x=-213
x = float(x)
y=(3*x**3)-(2*x**2)+(3*x)-1
print("y =", y)



"""_----------------------------------------------------------_"""



#TASK 7 :
#this program computes the number of seconds in a given number of hours

a = 2 # number of hours
seconds = 3600 # number of seconds in 1 hour

print("Hours: ", a) #printing the number of hours
print("Seconds in Hours: ", a * seconds) # printing the number of seconds in a given number of hours
print("Goodbye")
#this is the end of the program that computes the number of seconds in 3 hour






"""_----------------------------------------------------------_"""


#TASK 8 :

x= float(7)# input a float value for variable a here
y= float(9)# input a float value for variable b here

sum = x+y# output the result of addition here
sub = x-y# output the result of subtraction here
mul = x*y# output the result of multiplication here
div = x/y# output the result of division here

print(f" addition = {sum},\n subtraction = {sub},\n multiplication = {mul},\n division = {div}\nThat's all, folks!")





"""_----------------------------------------------------------_"""


#TASK 9 :

x = float(input("Enter value for x: "))

y=1/(x+(1/(x+(1/(x+(1/x))))))
print("y =", y)





"""_----------------------------------------------------------_"""




#TASK 10:

hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

# Write your code here.
durationhours = dura/60+hour
minutes = (mins + dura) %60
hours = int(hour + (mins +dura) / 60) % 24

print(hours,":",minutes,sep="")