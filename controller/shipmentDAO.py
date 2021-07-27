from models.shippment import Shipment

class ShipmentDAO:
    def __init__(self):
       self.shiList = {}

    def add_shipment(self, shippmentID, shippeditem, retailcenter):
        assert self.__check_unique_id__(shippmentID), "The id is not unique"
        assert self.__check_unique_shipped_item__(shippeditem), "The shippeditem and shippment is not satified with one - one relationship"

        shi = Shipment(shippmentID, shippeditem, retailcenter)
        self.shiList[shippmentID] = shi


    def get_shi_by_id(self, id):
        if id in self.shiList.keys():
            return self.shiList[id]
        return None

    def print_shilist(self):
        print("LIST OF SHIPMENTS: ")
        for shi in self.shiList.items():
            print(shi[1])
        print()

    def get_dict_list(self):
        shidictlist = []
        for shi in self.shiList.items():
            shidictlist.append(shi[1].get_infor_dist())
        return shidictlist


    def __check_unique_id__(self, id):
        if id in self.shiList.keys():
            return False
        return True

    def __check_unique_shipped_item__(self, shippeditem):
        for shi in self.shiList:
            if shi.get_itemnumID() == shippeditem.get_itemnum():
                return False
        return True
