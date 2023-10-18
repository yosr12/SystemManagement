from datetime import datetime


class Consumer : 
    """
    This class represents a Consumer of energy of a houshold.

    Args:
        name (str): The name of the consumer.
        energyNeed (float): The energy need of the consumer in units.

    Attributes:
        name (str): The name of the consumer.
        energyNeed (float): The energy need of the consumer.
        timestamp (str): Timestamp when energy need was last updated.

    Methods:
        set_energy_need(energyNeed): Set the energy need of the consumer and update the timestamp.

    """
    def __init__(self , name ,energyNeed) : 
        self.name = name 
        self.energyNeed = energyNeed
        self.timestamp = None

    def set_energyNeed(self, energyNeed):
        """
        TRhis method is to set the energy need of the consumer and update the timestamp.
        """
        self.energyNeed = energyNeed
        current_datetime = datetime.now()
        self.timestamp = current_datetime.strftime("(%d/%m/%Y %H:%M:%S)")