

class Vechile_TransportEvent:
    def __init__(self, vechile, transevent):

        self.__check_type__(vechile, transevent)

        self.vechileID = vechile.get_vechileID()
        self.schedulenum = transevent.get_schedulenum()


    def __check_type__(self, vechile, transevent):
        assert str(type(vechile)) == "<class 'models.vechile.Vechile'>", "Wrong format"
        assert str(type(transevent)) == "<class 'models.transportenvet.TransportEvent'>", "Wrong format"


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
