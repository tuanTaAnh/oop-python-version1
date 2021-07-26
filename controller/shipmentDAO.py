from models.shippment import Shipment

class ShipmentDAO:
    def __init__(self):
       self.shiList =  []

    def add_shipment(self, shippmentID, shippeditem, retailcenter):
        assert self.__check_unique_id(shippmentID), "The id is not unique"
        assert self.__check_unique_shipped_item(shippeditem), "The shippeditem and shippment is not satified with one - one relationship"

        shi = Shipment(shippmentID, shippeditem, retailcenter)
        self.shiList.append(shi)


    def get_shi_by_id(self, id):
        for shi in self.shiList:
            if shi.get_shippmentID() == id:
                return shi
        return None

    def print_shilist(self):
        print("LIST OF SHIPMENTS: ")
        for shi in self.shiList:
            print(shi)
        print()

    def get_dict_list(self):
        shidictlist = []
        for shi in self.shiList:
            shidictlist.append(shi.get_infor_dist())
        return shidictlist


    def __check_unique_id(self, id):
        for shi in self.shiList:
            if shi.shippmentID == id:
                return False
        return True

    def __check_unique_shipped_item(self, shippeditem):
        for shi in self.shiList:
            if shi.get_itemnumID() == shippeditem.get_itemnum():
                return False
        return True
