from Components import CleanEnergyProducer, Consumer , Battery , Grid
import logging


"""
    Energy Management System for a household.
    Manages the flow of energy between CleanEnergyProducer, Battery, Consumer, and Grid.

    Args:
        Battery: An instance of the Battery class.
        CleanEnergyProducer: An instance of the CleanEnergyProducer class.
        Consumer: An instance of the Consumer class.
        Grid: An instance of the Grid class.

    Attributes:
        battery (Battery): The battery component.
        cleanEnergyProducer (CleanEnergyProducer): The clean energy producer component.
        consumer (Consumer): The consumer component.
        grid (Grid): The grid component.
        
        logger (logging.Logger): Logger for recording energy management activities.
    """

class enegery_Management : 
    def __init__(self, Battery , CleanEnergyProducer , Consumer, Grid) : 
        self.battery = Battery
        self.cleanEnergyProducer = CleanEnergyProducer 
        self.consumer = Consumer
        self.grid = Grid
        self.logger = self.setup_logger()

    def setup_logger(self):

        """
        Set up a logger for recording energy management activities.
        """
        logger = logging.getLogger("EnergyManagement")
        logger.setLevel(logging.INFO)
        file_handler = logging.FileHandler("energy_management.log")
        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        return logger

    


    def management(self) :
        """
        Manage the flow of energy between components based on availability and demand.
        """
        grid_energy = 0
        stock_energy = 0
        self.logger.info("Start Management operation completed.")
        if (self.cleanEnergyProducer.capacity > 0 ):
            if (self.consumer.energyNeed < self.cleanEnergyProducer.capacity) :
                self.cleanEnergyProducer.energyProvided = self.consumer.energyNeed
                self.cleanEnergyProducer.capacity = self.cleanEnergyProducer.capacity - self.cleanEnergyProducer.energyProvided
                self.logger.info("Energy from cleanEnergyProducer")
                if (self.battery.energyLevel == 0):
                    stock_energy=self.battery.stock_Energy(self.cleanEnergyProducer.capacity)
                    self.logger.info("Charging Battery from cleanEnergyProducer ")
                elif(self.battery.energyLevel != 0) :   
                    stock_energy=self.battery.stock_Energy(self.cleanEnergyProducer.capacity - self.battery.energyLevel)
                    self.logger.info("Charging rest of battery Battery from cleanEnergyProducer  ")
                else :
                    print("full battery")  
            else : 
                if (self.consumer.energyNeed < self.battery.energyLevel) :
                    self.battery.provide_Energy(self.consumer.energyNeed - self.cleanEnergyProducer.capacity)
                else :
                    self.grid.connection_Grid()
                    grid_energy=self.grid.get_Grid_Energy(self.consumer.energyNeed - self.battery.energyLevel)
                    self.logger.info("Energy from Grid")
        elif(self.cleanEnergyProducer.capacity == 0  and self.battery.energyLevel != 0):
            if (self.consumer.energyNeed < self.battery.energyLevel) :
                self.battery.provide_Energy(self.consumer.energyNeed)
            else :
                self.grid.connection_Grid()
                grid_energy=self.get_Grid_Energy(self.consumer.energyNeed - self.battery.energyLevel)
                self.logger.info("Energy from Grid")
        elif(self.cleanEnergyProducer.capacity == 0  and self.battery.energyLevel == 0) :
            self.grid.connection_Grid()
            grid_energy=self.grid.get_Grid_Energy(self.consumer.energyNeed)        
            self.logger.info("Energy from Grid")

        self.logger.info("Management operation completed.")
        print(stock_energy,grid_energy)
        return stock_energy,grid_energy



                

        

