def read_int(prompt, min, max):
    try:
        theNum = int(input(prompt))
        if theNum in range(min, max+1):
            return theNum
    except ValueError: 
            return "Error: wrong input. The value is not within the permitted range (-10..10)"
            readint(prompt, min, max)



v = read_int("Enter a number from -10 to 10: ", -10, 10)

print("The number is:", v)