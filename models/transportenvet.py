

class TransportEvent:
    def __init__(self, schedulenum, typ, deliveryRoute):

        self.__check_type__(schedulenum, typ, deliveryRoute)

        self.__schedulenum__ = schedulenum
        self.typ = typ
        self.deliveryRoute = deliveryRoute


    def __check_type__(self, schedulenum, typ, deliveryRoute):
        assert type(schedulenum) == str, "Wrong format"
        assert type(typ) == str, "Wrong format"
        assert type(deliveryRoute) == str, "Wrong format"


    # getter method
    def get_schedulenum(self):
        return self.__schedulenum__

    # getter method
    def get_typ(self):
        return self.typ

    # getter method
    def get_deliveryRoute(self):
        return self.deliveryRoute


    # setter method
    def set_schedulenum(self, schedulenum):
        self.__schedulenum__ = schedulenum

    # setter method
    def set_typ(self, typ):
        self.typ = typ

    # setter method
    def set_deliveryRoute(self, deliveryRoute):
        self.deliveryRoute = deliveryRoute


    def __str__(self):
        return self.__schedulenum__ + ", " + self.typ + ", " + self.deliveryRoute + "."
