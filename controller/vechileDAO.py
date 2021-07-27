from models.vechile import Vechile

class VechileDAO:
    def __init__(self):
       self.vecList =  {}

    def add_vechile(self, vechileID, fuel_per_km, branch):
        assert self.__check_unique_id(vechileID), "The id is not unique"

        vec = Vechile(vechileID, fuel_per_km, branch)
        self.vecList[vechileID] = vec

    def get_vec_by_id(self, id):
        if id in self.vecList.keys():
            return self.vecList[id]
        return None

    def print_veclist(self):
        print("LIST OF VECHILES: ")
        for vec in self.vecList.items():
            print(vec[1])
        print()

    def get_dict_list(self):
        vecdictlist = []
        for vec in self.vecList.items():
            vecdictlist.append(vec[1].get_infor_dist())
        return vecdictlist


    def __check_unique_id(self, id):
        if id in self.vecList.keys():
            return False
        return True
