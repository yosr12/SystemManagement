class CleanEnergyProducer:

    """
     This class represents a Clean Energy Producer.

    Args:
        type (str): The type of clean energy producer (ex: solar, wind).
        capacity (float): The maximum capacity of the producer in units.

    Attributes:
        type (str): The type of clean energy producer.
        capacity (float): The maximum capacity of the producer.
        energyProvided (float): The energy provided by the producer.

    Methods:
        produce_energy(energy): Produces energy and updates the energyProvided attribute.

    """

    def __init__(self, type , capacity) : 
        self.type = type
        self.capacity = capacity
        self.energyProvided = 0
        print('hello from CEP')

    def produce_energy(self, energy):
        """
        Produces energy and updates the energyProvided attribute.

        """
        self.energyProvided += energy







            




