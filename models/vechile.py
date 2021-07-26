

class Vechile:
    def __init__(self, vechileID, fuel_per_km, branch):

        self.__check_type__(vechileID, fuel_per_km, branch)

        self.__vechileID__ = vechileID
        self.fuel_per_km = fuel_per_km
        self.branch = branch


    def __check_type__(self, vechileID, color, branch):
        assert type(vechileID) == str, "Wrong format"
        assert type(color) == str, "Wrong format"
        assert type(branch) == str, "Wrong format"


    # getter method
    def get_vechileID(self):
        return self.__vechileID__

    # getter method
    def get_fuel_per_km(self):
        return self.fuel_per_km

    # getter method
    def get_branch(self):
        return self.branch


    # setter method
    def set_vechileID(self, vechileID):
        self.__vechileID__ = vechileID

    # setter method
    def set_fuel_per_km(self, fuel_per_km):
        self.fuel_per_km = fuel_per_km

    # setter method
    def set_branch(self, branch):
        self.branch = branch


    def __str__(self):
        return self.__vechileID__ + ", " + self.fuel_per_km + ", " + self.branch + "."
