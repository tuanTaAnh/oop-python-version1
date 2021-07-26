

class Shipment:
    def __init__(self, shippmentID, shippeditem, retailcenterlist):
        self.shippmentID = shippmentID
        self.itemnumID = shippeditem.itemnum
        self.retailcenterlist = retailcenterlist


    # getter method
    def get_shippmentID(self):
        return self.shippmentID

    # getter method
    def get_itemnumID(self):
        return self.itemnumID

    # getter method
    def get_retailcenterID(self):
        return self.retailcenterlist


    # setter method
    def set_shippmentID(self, shippmentID):
        self.shippmentID = shippmentID

    # setter method
    def set_itemnumID(self, shippeditem):
        self.itemnumID = shippeditem.itemnum

    # setter method
    def set_retailcenterID(self, retailcenterlist):
        self.retailcenterlist = retailcenterlist


    def __str__(self):
        self.retailcenterIDlist  = "list of retailcenterIDs: "
        for center in self.retailcenterlist:
            self.retailcenterIDlist += center.uniqueID
            self.retailcenterIDlist += " "
        return self.shippmentID + ", " + self.itemnumID + ", " + self.retailcenterIDlist + "."
