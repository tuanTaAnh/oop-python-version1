

class ShippedItem:
    def __init__(self, itemnum, weight, dims, insur_amount, destination, finaldeldate):
        self.itemnum = itemnum
        self.weight = weight
        self.dims = dims
        self.insur_amount = insur_amount
        self.destination = destination
        self.finaldeldate = finaldeldate


    # getter method
    def get_itemnum(self):
        return self.itemnum

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
        self.itemnum = itemnum

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


    def get_infor(self):
        return self.itemnum + ", " + self.weight + ", " + self.dims + ", " + self.insur_amount + ", " + str(self.destination) + ", " + str(self.finaldeldate) + "."
