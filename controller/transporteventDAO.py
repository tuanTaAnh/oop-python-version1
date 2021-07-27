from models.transportenvet import TransportEvent

class TransportEventDAO:
    def __init__(self):
       self.tranList =  {}

    def add_tran(self, schedulenum, typ, deliveryRoute):
        assert self.__check_unique_id(schedulenum), "The id is not unique"

        tran = TransportEvent(schedulenum, typ, deliveryRoute)
        self.tranList[schedulenum] = tran

    def get_tran_by_id(self, id):
        if id in self.tranList.keys():
            return self.tranList[id]
        return None

    def print_tranlist(self):
        print("LIST OF TRANSPORT EVENTS: ")
        for tran in self.tranList.items():
            print(tran[1])
        print()

    def get_dict_list(self):
        trandictlist = []
        for tran in self.tranList.items():
            trandictlist.append(tran[1].get_infor_dist())
        return trandictlist


    def __check_unique_id(self, id):
        if id in self.tranList.keys():
            return False
        return True


