class Vehicle:

    def __init__(self, year, make, model):
        self.year = year
        self.make = make
        self.model = model

    def __eq__(self, other):
        if not isinstance(other, Vehicle):
            return False
        return self.year == other.year and self.make == other.make and self.model == other.model