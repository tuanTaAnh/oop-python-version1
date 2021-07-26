from models.vechile import Vechile

class VechileDAO:
    def __init__(self):
       self.vecList =  []

    def add_vechile(self, vechileID, fuel_per_km, branch):
        assert self.__check_unique_id(vechileID), "The id is not unique"

        vec = Vechile(vechileID, fuel_per_km, branch)
        self.vecList.append(vec)

    def get_vec_by_id(self, id):
        for vec in self.vecList:
            if vec.get_vechileID() == id:
                return vec
        return None

    def print_veclist(self):
        print("LIST OF VECHILES: ")
        for vec in self.vecList:
            print(vec)
        print()

    def get_dict_list(self):
        vecdictlist = []
        for vec in self.vecList:
            vecdictlist.append(vec.get_infor_dist())
        return vecdictlist


    def __check_unique_id(self, id):
        for vec in self.vecList:
            if vec.vechileID == id:
                return False
        return True
