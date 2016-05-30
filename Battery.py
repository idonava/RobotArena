import GlobalParameters as GP


class Battery:

    def __init__(self):
        self.bat=float(GP.batteryFull)

    def charge(self):
        self.bat=min(100,self.bat + GP.BatteryCharge)

    def unCharge(self):
        self.bat = max(0, self.bat - GP.BatteryCharge)
