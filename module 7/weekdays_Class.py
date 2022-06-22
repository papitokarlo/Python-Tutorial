#TASK2 2:

class WeekDayError(Exception):
    pass
	

class Weeker:
    WEEK_DAYS = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
    def __init__(self, day):
        try:
            self.__current = self.WEEK_DAYS.index(day)
        except ValueError:
            raise WeekDayError
                    
    def __str__(self):
        return self.WEEK_DAYS[self.__current]

    def add_days(self, n):
        self.__current = (self.__current + n) % 7

    def subtract_days(self, n):
        self.__current = (self.__current - n) % 7


try:
    weekday = Weeker('Mon')
    print(weekday)
    weekday.add_days(15)
    print(weekday)
    weekday.subtract_days(23)
    print(weekday)
    weekday = Weeker('Monday')
except WeekDayError:
    print("Sorry, I can't serve your request.")
