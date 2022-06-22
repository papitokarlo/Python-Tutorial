#TASK 2 :

def is_year_leap(year):
    leap = False
    
    if year%400==0 :
        leap = True
    elif year%4 == 0 and year%100 != 0:
        leap = True
    return leap


test_data = [1900, 2000, 2016, 1987]
test_results = [False, True, True, False]
for i in range(len(test_data)):
	yr = test_data[i]
	print(yr,"->",end="")
	result = is_year_leap(yr)
	if result == test_results[i]:
		print("OK")
	else:
		print("Failed")






"""_----------------------------------------------------------_"""



#TASk 3 :
def is_year_leap(year):
    leap = False
    
    if year%400==0 :
        leap = True
    elif year%4 == 0 and year%100 != 0:
        leap = True
    return leap


def days_in_month(year, month):
    if month in {1, 3, 5, 7, 8, 10, 12}:
        return 31

    elif month==2:
        if is_year_leap(year):
            return 29
        else:
            return 28
    elif month in {4,6,8,9,11}:
        return 30
    else:
        return None

test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
	yr = test_years[i]
	mo = test_months[i]
	print(yr, mo, "->", end="")
	result = days_in_month(yr, mo)
	if result == test_results[i]:
		print("OK")
	else:
		print("Failed")






#TASK 4 : 
#Check for leap year
def is_year_leap(year):
    if year%400==0 or (year%100 != 0 and year%4==0):
        return True
    else:
        return False

#Check for number of days in month
def days_in_month(year, month):
    month31=[1,3,5,7,8,10,12]
    if month in month31:
        return 31
    elif(month == 2):
        if(is_year_leap(year)):
            return 29
        else:
            return 28
    else:
        return 30


#Check for corresponding day of the year
def day_of_year(year, month, day):
    total = 0
    if day <= days_in_month(year, month):
        total = day
        for i in range(month-1):
            total += days_in_month(year, i)
        return total
    else:
        return "Your month doesn't have that many days."


print(day_of_year(2000, 12, 31))






#TASK 5 :

def is_prime(x):
    if (x > 1):
        divisor = 2

        for i in range(divisor,x):
            if (x % i) == 0:
                return False
    else:
        return False

    return True

for i in range(1, 20):
	if is_prime(i + 1):
			print(i + 1, end=" ")
print()





#TASK 6:

def liters_100km_to_miles_gallon(liters):
    kms_per_mile=1.609344
    liters_per_gallon=3.785411784
    kms_per_liter=100/liters
    kms_per_gallon=kms_per_liter*liters_per_gallon
    miles_per_gallon=kms_per_gallon/kms_per_mile
    return miles_per_gallon


def miles_gallon_to_liters_100km(miles):
    kms_per_mile=1.609344
    liters_per_gallon=3.785411784
    gallons_per_100miles=100/miles
    gallons_per_100kms=gallons_per_100miles/kms_per_mile
    liters_per_100kms=gallons_per_100kms*liters_per_gallon
    return liters_per_100kms


print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))

