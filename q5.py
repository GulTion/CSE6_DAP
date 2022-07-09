class Point:
    def __init__(self, x, y):
        if(x == None and y==None): x,y=0,0
        self.x = x; self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"


p = Point(3,34)

print(p)
