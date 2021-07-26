

class Vechile:
    def __init__(self, vechileID, color, branch):
        self.vechileID = vechileID
        self.color = color
        self.branch = branch


    # getter method
    def get_vechileID(self):
        return self.vechileID

    # getter method
    def get_color(self):
        return self.color

    # getter method
    def get_branch(self):
        return self.branch


    # setter method
    def set_vechileID(self, vechileID):
        self.vechileID = vechileID

    # setter method
    def set_color(self, color):
        self.color = color

    # setter method
    def set_branch(self, branch):
        self.branch = branch


    def __str__(self):
        return self.vechileID + ", " + self.color + ", " + self.branch + "."
