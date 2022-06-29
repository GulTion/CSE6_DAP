import datetime as dt

# print(dt.date.today().day)


class user:
    _login = False
    data = {}

    def __init__(self, password, timestamp=dt.date.today()):
        self.password = password
        self.timestamp = timestamp
        self.modifyuser = self.modifyuser(self)

    def login(self, password):
        self._login = self.password == password
        if(self._login):
            print("user is login")
        else:
            print("Wrong Password")

    def logout(self):
        self._login = False
        print("user is logout")

    def setdata(self, key, value):
        if(not self._login):
            print("Not Authorized, login first !")
            pass
        else:
            self.data[key] = value

    def display(self):
        if(not self._login):
            print("Not Authorized, login first !")
            pass
        for key, value in self.data.items():
            print(key, ":", value)

    class modifyuser:

        def __init__(self, parent):
            self.parent = parent

        def diff_month(self, d1, d2):
            return (d1.year - d2.year) * 12 + d1.month - d2.month

        def modifypassword(self, password):
            if(not self.parent._login):
                print("Not Authorized, login first !")
                pass

            else:
                month_rest = self.diff_month(
                    dt.date.today(), self.parent.timestamp)
                if(month_rest > 12 and self.parent.password != password):
                    self.parent.password = password
                    self.parent.timestamp = dt.date.today()
                else:
                    print("same password will use after", month_rest, "month")


a = user("GOD")
a.login("GOD")
a.setdata("name", "Gulshan")
a.setdata("age", "20")
# a.timestamp = dt.date(2021, 1, 1)
a.display()
a.modifyuser.modifypassword("HEsddY")

print(a.password)


# print(diff_month(b, a))
