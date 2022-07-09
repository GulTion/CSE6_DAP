
class complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag
    def __add__(self, b):
        return complex(self.real+b.real, self.imag+b.imag)
    
    def __str__(self):
        return f"({self.real}, {self.imag})"


a = complex(3,3)
b = complex(4,35)

print(a+b)

