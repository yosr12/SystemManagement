
from datetime import datetime


class consumer : 
    def __init__(self , name ,energyNeed) : 
        self.name = name 
        self.energyNeed = energyNeed
        self.timestamp = None

    def set_energyNeed(self, energyNeed):
        self.energyNeed = energyNeed
        current_datetime = datetime.now()
        self.timestamp = current_datetime.strftime("(%d/%m/%Y %H:%M:%S)")