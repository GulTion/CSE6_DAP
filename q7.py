class Device:
    def processDoc(self):
        print("this is a device")
        

class Scanner(Device):
    def processDoc(self):
        print("this is a scanner")


class Copier(Device):
    def processDoc(self):
        print("this is a copier")


class ComboDevice(Scanner, Copier):
    def processDoc(self):
        print("this is a combo device")



a = Scanner()
a.processDoc()

b = Copier()
b.processDoc()

c = ComboDevice()
c.processDoc()

# print(a)
