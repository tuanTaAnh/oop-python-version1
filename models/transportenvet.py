

class TransportEvent:
    def __init__(self, schedulenum, typ, deliveryRoute):
        self.schedulenum = schedulenum
        self.typ = typ
        self.deliveryRoute = deliveryRoute


    # getter method
    def get_schedulenum(self):
        return self.schedulenum

    # getter method
    def get_typ(self):
        return self.typ

    # getter method
    def get_deliveryRoute(self):
        return self.deliveryRoute


    # setter method
    def set_schedulenum(self, schedulenum):
        self.schedulenum = schedulenum

    # setter method
    def set_typ(self, typ):
        self.typ = typ

    # setter method
    def set_deliveryRoute(self, deliveryRoute):
        self.deliveryRoute = deliveryRoute


    def __str__(self):
        return self.schedulenum + ", " + self.typ + ", " + self.deliveryRoute + "."
