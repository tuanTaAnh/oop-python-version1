

class Vechile_TransportEvent:
    def __init__(self, vechile, transevent):
        self.vechileID = vechile.vechileID
        self.schedulenum = transevent.schedulenum


    # getter method
    def get_vechileID(self):
        return self.vechileID

    # getter method
    def get_schedulenum(self):
        return self.schedulenum


    # setter method
    def set_shippmentID(self, vechile):
        self.vechileID = vechile.vechileID

    # setter method
    def set_schedulenum(self, transevent):
        self.shippmentID = transevent.schedulenum


    def __str__(self):
        return self.vechileID + ", " + self.schedulenum + "."
