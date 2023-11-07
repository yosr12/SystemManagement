from Components import CleanEnergyProducer, Consumer , Battery , Grid
import Energy_Management
import pandas as pd


def calcul_Total_Energy(new_Energy,total_Energy) :
    """
    Calculate the total energy by adding the new energy to the existing total energy.
    (tested on two different clean energyProducers and also two Batteries)

    """ 
    total_Energy = total_Energy +new_Energy
    return total_Energy
    

def main():

    # CRP = CleanEnergyProducer.cleanEnergyProducer('solar', 0)
    # bat = Battery.battery(1000)
    # cons = Consumer.consumer('household' , 200)
    # Gr = Grid.grid(10 ,200,300)
    # EM = Energy_Management.enegery_Management(bat,CRP,cons,Gr)
    # bat.stock_Energy(800)
    # EM.management()
    ####################################################################
    # Specify the CSV file path
    csv_file = 'profiles_dataset.csv'
    # Read the CSV file into a DataFrame
    dataframe = pd.read_csv(csv_file)
    # Create empty lists to store battery level and grid energy values
    battery_level_values = []
    Grid_values = []
    print('hey')

    #iterate over the dataframe
    for index, row in dataframe.iterrows():
        timestamp = row['timestamp']
        pv_yield_power = row['pv_yield_power']
        household_consumption = row['household_consumption']
        CRP = CleanEnergyProducer.CleanEnergyProducer('solar', pv_yield_power)
        bat = Battery.Battery(80000)
        Gr = Grid.Grid(10)
        cons = Consumer.Consumer('household' , household_consumption)
        EM = Energy_Management.enegery_Management(bat,CRP,cons,Gr)
        # Perform energy management and get results
        stock_energy,grid_energy=EM.management()
        Grid_values.append(grid_energy)
        battery_level_values.append(stock_energy)

# Add the battery_level column to the DataFrame
    dataframe['battery_level'] = battery_level_values
    dataframe['Grid_energy'] = Grid_values
# Save the updated DataFrame back to the CSV file
    dataframe.to_csv(csv_file, index = False)


        


   
if __name__ == "__main__":
    main()















"""
Manually Testing of the different classes
"""


 # print(Energy_Management.enegery_Management())
    # print("hello")
    # total_Energy = 0
    # total_Energy_Battery = 0
    # solar = CleanEnergyProducer.cleanEnergyProducer('solar' , 15000)
    # wind = CleanEnergyProducer.cleanEnergyProducer('wind' , 15000)
    # fridge = Consumer.consumer('fridge' , 1000)
    # total_Energy= calcul_Total_Energy(solar.capacity,total_Energy)
    # print(calcul_Total_Energy(wind.capacity,total_Energy))

    # b = Battery.battery(1000)
    # b1 = Battery.battery(1200)
    # b.stock_Energy(900)
    # total_Energy_Battery = calcul_Total_Energy(b.energyLevel,total_Energy_Battery)
    # print(total_Energy_Battery,"aaaa")
    # b1.stock_Energy(1100)
    # print(b1.energyLevel)
    # total_Energy_Battery= calcul_Total_Energy(b1.energyLevel,total_Energy_Battery)
    # print(total_Energy_Battery,"aaa")
    # print(b.energyLevel)
    # y = Grid.grid(12,1000,1200)
    # print(y.status)
    # y.connection_Grid()
    # print(y.get_Grid_Energy(100))

    # print(y.costs)
   