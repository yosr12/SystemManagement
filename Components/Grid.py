

class grid : 
    def __init__(self, electricity_price):
        self.status = False 
        self.electricity_price = electricity_price       
        self.costs = 0

    def connection_Grid(self):
        self.status = True
        print("Grid Connected")
    def desconnection_Grid(self) : 
        self.status = False
        print("Grid desconnected")

    def get_Grid_Energy(self , energy) : 
        if (self.status):
            self.costs = energy*self.electricity_price
            return energy


    def get_Electricity_Price(self):
        return self.electricity_price
