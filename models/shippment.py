

class Shipment:
    def __init__(self, shippmentID, shippeditem, retailcenter):
        self. __check_type__(shippmentID, shippeditem, retailcenter)

        self.__shippmentID__ = shippmentID
        self.itemnumID = shippeditem.get_itemnum()
        self.retailcenterID = retailcenter.get_uniqueID()

    def __check_type__(self, shippmentID, shippeditem, retailcenter):
        assert type(shippmentID) == str, "Wrong format"
        assert str(type(shippeditem)) == "<class 'models.shippeditem.ShippedItem'>", "Wrong format"
        assert str(type(retailcenter)) == "<class 'models.retailcenter.RetailCenter'>", "Wrong format"


    # getter method
    def get_shippmentID(self):
        return self.__shippmentID__

    # getter method
    def get_itemnumID(self):
        return self.itemnumID

    # getter method
    def get_retailcenterID(self):
        return self.retailcenterID


    # setter method
    def set_shippmentID(self, shippmentID):
        self.__shippmentID__ = shippmentID

    # setter method
    def set_itemnumID(self, shippeditem):
        self.itemnumID = shippeditem.itemnum

    # setter method
    def set_retailcenterID(self, retailcenter):
        self.retailcenterID = retailcenter.uniqueID


    def __str__(self):
        return self.__shippmentID__ + ", " + self.itemnumID + ", " + self.retailcenterID + "."
