from models.shippeditem import ShippedItem

class ShippedItemDAO:
    def __init__(self):
       self.itemList =  {}

    def add_item(self, itemnum, weight, dims, insur_amount, destination, finaldeldate):
        assert self.__check_unique_id__(itemnum), "The id is not unique"

        recenter = ShippedItem(itemnum, weight, dims, insur_amount, destination, finaldeldate)
        self.itemList[itemnum] = recenter


    def get_item_by_id(self, id):
        if id in self.itemList.keys():
            return self.itemList[id]
        return None

    def print_itemlist(self):
        print("LIST OF ITEMS: ")
        for ite in self.itemList.items():
            print(ite[1])
        print()

    def get_dict_list(self):
        itemdictlist = []
        for ite in self.itemList[0]:
            itemdictlist.append(ite[1].get_infor_dist())
        return itemdictlist


    def __check_unique_id__(self, id):
        if id in self.itemList.keys():
            return False
        return True
