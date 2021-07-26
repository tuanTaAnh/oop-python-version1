from models.shippeditem import ShippedItem

class ShippedItemDAO:
    def __init__(self):
       self.itemList =  []

    def add_item(self, itemnum, weight, dims, insur_amount, destination, finaldeldate):
        assert self.__check_unique_id(itemnum), "The id is not unique"

        recenter = ShippedItem(itemnum, weight, dims, insur_amount, destination, finaldeldate)
        self.itemList.append(recenter)


    def get_item_by_id(self, id):
        for item in self.itemList:
            if item.get_itemnum() == id:
                return item
        return None

    def print_itemlist(self):
        print("LIST OF ITEMS: ")
        for item in self.itemList:
            print(item)
        print()

    def get_dict_list(self):
        recenterdictlist = []
        for item in self.itemList:
            recenterdictlist.append(item.get_infor_dist())
        return recenterdictlist


    def __check_unique_id(self, id):
        for item in self.itemList:
            if item.uniqueID == id:
                return False
        return True
