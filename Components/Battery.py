


class battery:
    def __init__(self, capacity) : 
        self.capacity = capacity 
        # self.energyLimit = energyLimit
        self.energyLevel = 0.0

    def stock_Energy(self,energy):
        if (self.capacity > energy) : 
            self.energyLevel += energy
            return self.energyLevel

    def provide_Energy(self, energy):
        if (self.energyLevel > 0 ) : 
            self.energyLevel -= energy

    def get_Energy_Level(self):
        return self.energyLevel

    def get_Capacity(self):
        return self.capacity        



