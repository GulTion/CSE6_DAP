
class mycomplex(complex):
    def __add__(self, b):
        return mycomplex(self.real * b.real, self.imag * b.imag)


a = mycomplex(3,3)
b = mycomplex(4,35)



print(a+b)