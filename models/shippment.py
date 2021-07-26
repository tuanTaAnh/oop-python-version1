

class Shipment:
    def __init__(self, shippmentID, shippeditem, retailcenter):
        self.shippmentID = shippmentID
        self.itemnumID = shippeditem.itemnum
        self.retailcenterID = retailcenter.uniqueID


    # getter method
    def get_shippmentID(self):
        return self.shippmentID

    # getter method
    def get_itemnumID(self):
        return self.itemnumID

    # getter method
    def get_retailcenterID(self):
        return self.retailcenterID


    # setter method
    def set_shippmentID(self, shippmentID):
        self.shippmentID = shippmentID

    # setter method
    def set_itemnumID(self, shippeditem):
        self.itemnumID = shippeditem.itemnum

    # setter method
    def set_retailcenterID(self, retailcenter):
        self.retailcenterID = retailcenter.uniqueID


    def __str__(self):
        return self.shippmentID + ", " + self.itemnumID + ", " + self.retailcenterID + "."
