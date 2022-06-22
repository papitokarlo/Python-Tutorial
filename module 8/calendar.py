import calendar


class MyCalendar(calendar.Calendar):

    def __init__(self):
        self.setfirstweekday(calendar.SUNDAY)

    def count_weekday_in_year(self, year, weekday):
        counter = 0
        yearDays = []
        for x in range(1,13):
            yearDays.append(list(self.monthdays2calendar(year, x)))

        print("Working on the following list: \n", yearDays)

        for x in yearDays:
            for y in x:
                for z in y:
                    if z[1] == weekday:
                        counter+=1
        return counter


mc = MyCalendar()
print(mc.count_weekday_in_year(2000, 6))