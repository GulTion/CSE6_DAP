class Time:
    def __init__(self, h=0, m=0):
        self.hours = h
        self.minutes = m

    # (a)
    def addTime(self, t1, t2):
        minsum = t1.minutes+t2.minutes
        hoursum = t1.hours + t2.hours
        return Time(hoursum + (minsum)//60, (minsum) % 60)

    # (b)
    def displayTime(self):
        print(self)

    # (c)
    def displayMinute(self):
        print(f"{self.hours*60 + self.minutes} minute")

    def __str__(self):
        return f"{self.hours} hours and {self.minutes} minutes"


a = Time(2, 50)
b = Time(3, 20)

print(a.addTime(a, b))

a.displayTime()

a.displayMinute()