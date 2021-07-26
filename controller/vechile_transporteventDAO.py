from models.vechile_transportevent import Vechile_TransportEvent

class Vechile_TransportEventDAO:
    def __init__(self):
       self.vec_transList =  []

    def add_vec_trans(self, vechile, transevent):

        vec_trans = Vechile_TransportEvent(vechile, transevent)
        self.vec_transList.append(vec_trans)

    def get_vec_trans_by_id(self, vechile, transevent):
        for vec_trans in self.vec_transList:
            if vec_trans.get_vechileID() == vechile.vechileID and vec_trans.get_schedulenum() == transevent.schedulenum:
                return vec_trans
        return None

    def print_vec_trans_list(self):
        print("LIST OF VECHILE-TRANSPORT EVENT: ")
        for vec_trans in self.vec_transList:
            print(vec_trans)
        print()

    def get_dict_list(self):
        vec_transdictlist = []
        for vec_trans in self.vec_transList:
            vec_transdictlist.append(vec_trans.get_infor_dist())
        return vec_transdictlist


