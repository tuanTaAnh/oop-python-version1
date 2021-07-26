

class Shipment_TransportEvent:
    def __init__(self, shipment, transevent):
        self.shippmentID = shipment.shippmentID
        self.schedulenum = transevent.schedulenum


    # getter method
    def get_shipment(self):
        return self.shipment

    # getter method
    def get_schedulenum(self):
        return self.schedulenum


    # setter method
    def set_shippmentID(self, shipment):
        self.shippmentID = shipment.shippmentID

    # setter method
    def set_schedulenum(self, transevent):
        self.shippmentID = transevent.schedulenum


    def get_infor(self):
        return self.shippmentID + ", " + self.shippmentID + "."
