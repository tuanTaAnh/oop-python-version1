from models.retailcenter import RetailCenter

class RetailCenterDAO:
    def __init__(self):
       self.recenterList =  []

    def add_recenter(self, uniqueID, typ, address):
        assert self.__check_unique_id(uniqueID), "The id is not unique"

        recenter = RetailCenter(uniqueID, typ, address)
        self.recenterList.append(recenter)


    def get_recenter_by_id(self, id):
        for recenter in self.recenterList:
            if recenter.get_uniqueID() == id:
                return recenter
        return None

    def print_recenterlist(self):
        print("LIST OF RETAIL CENTERS: ")
        for recenter in self.recenterList:
            print(recenter)
        print()

    def get_dict_list(self):
        recenterdictlist = []
        for recenter in self.recenterList:
            recenterdictlist.append(recenter.get_infor_dist())
        return recenterdictlist


    def __check_unique_id(self, id):
        for recenter in self.recenterList:
            if recenter.uniqueID == id:
                return False
        return True
