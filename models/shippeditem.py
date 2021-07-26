

class ShippedItem:
    def __init__(self, itemnum, weight, dims, insur_amount, destination, finaldeldate):

        self.__check_type__(itemnum, weight, dims, insur_amount, destination, finaldeldate)

        self.__itemnum__ = itemnum
        self.weight = weight
        self.dims = dims
        self.insur_amount = insur_amount
        self.destination = destination
        self.finaldeldate = finaldeldate


    def __check_type__(self, itemnum, weight, dims, insur_amount, destination, finaldeldate):
        assert type(itemnum) == str, "Wrong format"
        assert type(weight) == int, "Wrong format"
        assert type(dims) == int, "Wrong format"
        assert type(insur_amount) == int, "Wrong format"
        assert type(destination) == str, "Wrong format"
        assert type(finaldeldate) == str, "Wrong format"


    # getter method
    def get_itemnum(self):
        return self.__itemnum__

    # getter method
    def get_weight(self):
        return self.weight

    # getter method
    def get_dims(self):
        return self.dims

    # getter method
    def get_insur_amount(self):
        return self.insur_amount

    # getter method
    def get_destination(self):
        return self.destination

    # getter method
    def get_finaldeldate(self):
        return self.finaldeldate


    # setter method
    def set_itemnum(self, itemnum):
        self.__itemnum__ = itemnum

    # setter method
    def set_weight(self, weight):
        self.weight = weight

    # setter method
    def set_dims(self, dims):
        self.dims = dims

    # setter method
    def set_insur_amount(self, insur_amount):
        self.insur_amount = insur_amount

    # setter method
    def set_destination(self, destination):
        self.destination = destination

    # setter method
    def set_finaldeldat(self, finaldeldat):
        self.finaldeldat = finaldeldat


    def __str__(self):
        return self.__itemnum__ + ", " + str(self.weight) + ", " + str(self.dims) + ", " + str(self.insur_amount) + ", " + str(self.destination) + ", " + str(self.finaldeldate) + "."
