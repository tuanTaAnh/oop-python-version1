from models.retailcenter import RetailCenter

class RetailCenterDAO:
    def __init__(self):
       self.recenterList =  {}

    def add_recenter(self, uniqueID, typ, address):
        assert self.__check_unique_id(uniqueID), "The id is not unique"

        recenter = RetailCenter(uniqueID, typ, address)
        self.recenterList[uniqueID] = recenter


    def get_recenter_by_id(self, id):
        if id in self.recenterList.keys():
            return self.recenterList[id]
        return None

    def print_recenterlist(self):
        print("LIST OF RETAIL CENTERS: ")
        for recenter in self.recenterList.items():
            print(recenter[1])
        print()

    def get_dict_list(self):
        recenterdictlist = []
        for recenter in self.recenterList.items():
            recenterdictlist.append(recenter[1].get_infor_dist())
        return recenterdictlist


    def __check_unique_id(self, id):
        if id in self.recenterList.keys():
            return False
        return True
