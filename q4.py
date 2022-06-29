class Time:
    def __init__(self, h=0, m=0):
        self.hours = h
        self.minutes = m

    def addTime(self, t1, t2):
        return Time(t1.hours + t2.hours + (t1.minutes+t2.minutes)//60, (t1.minutes+t2.minutes) % 60)

    def displayTime(self):
        print(self)
        return self

    def displayMinute(self):
        print(f"{self.hours*60 + self.minutes} minute")

    def __str__(self):
        return f"{self.hours} hours and {self.minutes} min"


a = Time(2, 50)
b = Time(1, 30)
a.addTime(a, b).displayTime()
a.displayMinute()
