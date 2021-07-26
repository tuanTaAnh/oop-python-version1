

class RetailCenter:
    def __init__(self, uniqueID, typ, address):

        self.__check_type__(uniqueID, typ, address)

        self.__uniqueID__ = uniqueID
        self.typ = typ
        self.address = address

    def __check_type__(self, uniqueID, typ, address):
        assert type(uniqueID) == str, "Wrong format"
        assert type(typ) == str, "Wrong format"
        assert type(address) == str, "Wrong format"

    # getter method
    def get_uniqueID(self):
        return self.__uniqueID__

    # getter method
    def get_typ(self):
        return self.typ

    # getter method
    def get_address(self):
        return self.address


    # setter method
    def set_uniqueID(self, uniqueID):
        self.__uniqueID__ = uniqueID

    # setter method
    def set_typ(self, typ):
        self.typ = typ

    # setter method
    def set_address(self, address):
        self.address = address


    def __str__(self):
        return self.__uniqueID__ + ", " + self.typ + ", " + self.address + "."
