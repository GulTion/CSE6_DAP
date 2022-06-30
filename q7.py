class Device:
    def processDoc(self):
        print("this is a device")
        pass


class Scanner(Device):
    def processDoc(self):
        print("this is a scanner")
        pass
    pass

class Copier(Device):
    def processDoc(self):
        print("this is a copier")
        pass


class ComboDevice(Scanner, Copier):
    def processDoc(self):
        print("this is a combo device")
        pass



a = Scanner().processDoc()

# print(a)
