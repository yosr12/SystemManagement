class Grid : 

    """
     This class represents the Grid component for energy supply.

    Args:
        electricity_price (float): The price of electricity per unit.

    Attributes:
        status (bool): Indicates whether the Grid is connected or disconnected.
        electricity_price (float): The price of electricity per unit.
        costs (float): The cost of energy from the Grid.

    Methods:
        connection_Grid(): Connects the Grid.
        disconnection_Grid(): Disconnects the Grid.
        get_Grid_Energy(energy): Retrieves energy from the Grid and calculates the cost.
        get_Electricity_Price(): Retrieves the electricity price.
    """
    def __init__(self, electricity_price):
        self.status = False 
        self.electricity_price = electricity_price       
        self.costs = 0

    def connection_Grid(self):
        """
        This method is to connect the Grid when needed
        """
        self.status = True
        print("Grid Connected")
    def desconnection_Grid(self) : 
        """
        This method is to disconnet the Grid"""
        self.status = False
        print("Grid desconnected")

    def get_Grid_Energy(self , energy) : 
        """
        Get energy from the grid and calculte its cost
        """
        if (self.status):
            self.costs = energy*self.electricity_price
            return energy


    def get_Electricity_Price(self):
        return self.electricity_price
def lambda_handler(event, context):
    # Assuming the Lambda function receives electricity_price as an event parameter
    electricity_price = float(event.get('electricity_price', 0.0))

    # Create a Grid instance
    grid = Grid(electricity_price)

    # Call the get_Electricity_Price method of the Grid instance
    electricity_price = grid.get_Electricity_Price()
    print('BBBBBB')
    return {
        'electricity_price': electricity_price
    }
