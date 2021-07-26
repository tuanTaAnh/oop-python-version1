

class Shipment_TransportEvent:
    def __init__(self, shipment, transevent):

        self.__check_type__(shipment, transevent)

        self.__shippmentID__ = shipment.get_shippmentID()
        self.__schedulenum__ = transevent.get_schedulenum()


    def __check_type__(self, shipment, transevent):
        assert str(type(shipment)) == "<class 'models.shippment.Shipment'>", "Wrong format"
        assert str(type(transevent)) == "<class 'models.transportenvet.TransportEvent'>", "Wrong format"

    # getter method
    def get_shipment(self):
        return self.__shippmentID__

    # getter method
    def get_schedulenum(self):
        return self.__schedulenum__

    # setter method
    def set_shippmentID(self, shipment):
        self.__shippmentID__ = shipment.get_shippmentID()

    # setter method
    def set_schedulenum(self, transevent):
        self.__shippmentID__ = transevent.get_schedulenum()

    def __str__(self):
        return self.__shippmentID__ + ", " + self.__schedulenum__ + "."
