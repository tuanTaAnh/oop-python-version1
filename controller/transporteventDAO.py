from models.transportenvet import TransportEvent

class TransportEventDAO:
    def __init__(self):
       self.tranList =  []

    def add_tran(self, schedulenum, typ, deliveryRoute):
        assert self.__check_unique_id(schedulenum), "The id is not unique"

        tran = TransportEvent(schedulenum, typ, deliveryRoute)
        self.tranList.append(tran)

    def get_tran_by_id(self, id):
        for tran in self.tranList:
            if tran.get_schedulenum() == id:
                return tran
        return None

    def print_tranlist(self):
        print("LIST OF TRANSPORT EVENTS: ")
        for tran in self.tranList:
            print(tran)
        print()

    def get_dict_list(self):
        trandictlist = []
        for tran in self.tranList:
            trandictlist.append(tran.get_infor_dist())
        return trandictlist


    def __check_unique_id(self, id):
        for tran in self.tranList:
            if tran.schedulenum == id:
                return False
        return True


