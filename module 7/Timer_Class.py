#TASK 2 TIMER CASSS::
class Timer:
    def __init__(self, hour=0, minute=0, second=0):
       self.h = hour
       self.min = minute
       self.sec = second

    def __str__(self):
        return f'{self.h:02}:{self.min:02}:{self.sec:02}'

    def next_second(self):
        if self.sec<59:
            self.sec+=1
            return self.sec
        elif self.sec == 59 and self.min<59:
            self.sec=0 
            self.min+=1
            return  self.sec, self.min
        else:
            self.sec=0 
            self.min=0
            if self.h<23:
                self.h+=1
                return self.h, self.min, self.sec
            else:
                self.h = 0
                return self.h, self.min, self.sec
        

    def prev_second(self):
        if self.sec>0:
            self.sec = self.sec-1
            return self.sec
        elif self.sec == 0 and self.min>0:
            self.sec=59
            self.min=self.min-1
            return  self.sec, self.min
        else:
            self.sec=59
            self.min=59
            if self.h == 0:
                self.h=23
                return self.h, self.min, self.sec
            else:
                self.h-=1
                return self.h, self.min, self.sec

timer = Timer(23, 59, 59)
print(timer)
timer.next_second()
print(timer)
timer.prev_second()
print(timer)
