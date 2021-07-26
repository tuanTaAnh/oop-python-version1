

class RetailCenter:
    def __init__(self, uniqueID, typ, address):
        self.uniqueID = uniqueID
        self.typ = typ
        self.address = address


    # getter method
    def get_uniqueID(self):
        return self.uniqueID

    # getter method
    def get_typ(self):
        return self.typ

    # getter method
    def get_address(self):
        return self.address


    # setter method
    def set_uniqueID(self, uniqueID):
        self.uniqueID = uniqueID

    # setter method
    def set_typ(self, typ):
        self.typ = typ

    # setter method
    def set_address(self, address):
        self.address = address


    def get_infor(self):
        return self.uniqueID + ", " + self.typ + ", " + self.address + "."
