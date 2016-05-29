
class Battery:

    def __init__(self):
        self.bat=float(100)

    def isEmpty(self):
        return (self.bat==0)

    def charge(self):
        self.bat=min(100,self.bat + 1)

    def unCharge(self):
        self.bat = max(0, self.bat - 1)
