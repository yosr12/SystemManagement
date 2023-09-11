


class Battery:
    """
     This class represents a Battery for energy storage.

    Args:
        capacity (float): The maximum capacity of the battery in units.

    Attributes:
        capacity (float): The maximum capacity of the battery.
        energyLevel (float): The current energy level of the battery.

    Methods:
        stock_energy(energy): Stock energy into the battery if capacity allows.
        provide_energy(energy): Provide energy from the battery if available.
        get_energy_level(): Get the current energy level of the battery.
        get_capacity(): Get the maximum capacity of the battery.

    """
    def __init__(self, capacity) : 
        self.capacity = capacity 
        # self.energyLimit = energyLimit
        self.energyLevel = 0.0

    def stock_Energy(self,energy):
        """
        Stock energy into the battery if capacity allows.
        """
        if (self.capacity > energy) : 
            self.energyLevel += energy
            return self.energyLevel

    def provide_Energy(self, energy):
        """
        Provide energy from the battery if available.
        """
        if (self.energyLevel > 0 ) : 
            self.energyLevel -= energy

    def get_Energy_Level(self):
        """
        Get the current energy level of the battery."""
        return self.energyLevel

    def get_Capacity(self):
        """
        Get the maximum capacity of the battery.
        """

        return self.capacity        



