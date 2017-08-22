from math import fabs
class times:
    def __init__(self,h,m,s):
        self.hours = h
        self.mins = m
        self.secs = s

    def __add__(self, other):
        hours = self.hours + other.hours
        mins = self.mins + other.mins
        secs = self.secs + other.secs

        if hours>=24:
            hours -= 24
        if mins>= 60:
            mins -= 60
        if secs>=60:
            secs -= 60
        return (fabs(hours),fabs(mins),fabs(secs))

    def __sub__(self, other):
        hours = self.hours - other.hours
        mins = self.mins - other.mins
        secs = self.secs - other.secs

        if hours>=24:
            hours -= 24
        if mins>= 60:
            mins -= 60
        if secs>=60:
            secs -= 60
        return (fabs(hours),fabs(mins),fabs(secs))


x = times(19,5,15)
y = times(6,45,45)
print(x+y)