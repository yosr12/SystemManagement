from Components import CleanEnergyProducer, Consumer , Battery , Grid
import logging
class enegery_Management : 
    def __init__(self, battery , cleanEnergyProducer , consumer, grid) : 
        self.battery = battery
        self.cleanEnergyProducer = cleanEnergyProducer 
        self.consumer = consumer
        self.grid = grid
        self.logger = self.setup_logger()

    def setup_logger(self):
        logger = logging.getLogger("EnergyManagement")
        logger.setLevel(logging.INFO)
        file_handler = logging.FileHandler("energy_management.log")
        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        return logger

    


    def management(self) :
        GE = 0
        SE = 0
        self.logger.info("Start Management operation completed.")
        if (self.cleanEnergyProducer.capacity > 0 ):
            if (self.consumer.energyNeed < self.cleanEnergyProducer.capacity) :
                self.cleanEnergyProducer.energyProvided = self.consumer.energyNeed
                self.cleanEnergyProducer.capacity = self.cleanEnergyProducer.capacity - self.cleanEnergyProducer.energyProvided
                self.logger.info("Energy from cleanEnergyProducer")
                if (self.battery.energyLevel == 0):
                    SE=self.battery.stock_Energy(self.cleanEnergyProducer.capacity)
                    self.logger.info("Charging Battery from cleanEnergyProducer ")
                elif(self.battery.energyLevel != 0) :   
                    SE=self.battery.stock_Energy(self.cleanEnergyProducer.capacity - self.battery.energyLevel)
                    self.logger.info("Charging rest of battery Battery from cleanEnergyProducer  ")
                else :
                    print("full battery")  
            else : 
                if (self.consumer.energyNeed < self.battery.energyLevel) :
                    # SE= self.battery.energyLevel
                    self.battery.provide_Energy(self.consumer.energyNeed - self.cleanEnergyProducer.capacity)
                else :
                    # SE= self.battery.energyLevel
                    self.grid.connection_Grid()
                    GE=self.grid.get_Grid_Energy(self.consumer.energyNeed - self.battery.energyLevel)
                    self.logger.info("Energy from Grid")
        elif(self.cleanEnergyProducer.capacity == 0  and self.battery.energyLevel != 0):
            # SE= self.battery.energyLevel
            if (self.consumer.energyNeed < self.battery.energyLevel) :
                self.battery.provide_Energy(self.consumer.energyNeed)
            else :
                # SE= self.battery.energyLevel
                self.grid.connection_Grid()
                GE=self.get_Grid_Energy(self.consumer.energyNeed - self.battery.energyLevel)
                self.logger.info("Energy from Grid")
        elif(self.cleanEnergyProducer.capacity == 0  and self.battery.energyLevel == 0) :
            # SE=self.battery.energyLevel == 0
            self.grid.connection_Grid()
            GE=self.grid.get_Grid_Energy(self.consumer.energyNeed)        
            self.logger.info("Energy from Grid")

        self.logger.info("Management operation completed.")
        print(SE,GE)
        return SE,GE



                

        

