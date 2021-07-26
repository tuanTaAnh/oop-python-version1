from models.shipment_transportevent import Shipment_TransportEvent

class Shipment_TransportEventDAO:
    def __init__(self):
       self.shi_tranList =  []

    def add_shi_tran(self, shipment, transevent):

        shi_tran = Shipment_TransportEvent(shipment, transevent)
        self.shi_tranList.append(shi_tran)

    def get_shi_tran_by_id(self, shipment, transevent):
        for shi_tran in self.shi_tranList:
            if shi_tran.get_shipment() == shipment.shippmentID and shi_tran.get_schedulenum() == transevent.schedulenum:
                return shi_tran
        return None

    def print_shi_tranlist(self):
        print("LIST OF SHIPMENT-TRANSPORT EVENT: ")
        for shi_tran in self.shi_tranList:
            print(shi_tran)
        print()

    def get_dict_list(self):
        shi_trandictlist = []
        for shi_tran in self.shi_tranList:
            shi_trandictlist.append(shi_tran.get_infor_dist())
        return shi_trandictlist


