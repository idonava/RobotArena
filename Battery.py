
class Battery:

    def __init__(self):
        self.bat=float(100)

    def charge(self):
        self.bat=min(100,self.bat + 2.4)

    def unCharge(self):
        self.bat = max(0, self.bat - 2.4)
