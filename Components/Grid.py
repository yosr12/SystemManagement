import boto3
ecr_client = boto3.client('ecr')

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
    try:
        # Replace 'firstcontainerformyproject' with your actual repository name
        repository_name = 'firstcontainerformyproject'

        # Get the list of images in the repository
        response = ecr_client.describe_images(
            repositoryName=repository_name
        )
        print('heyfromherhhhhhed')

        # Sort the images by imagePushedAt timestamp in descending order
        sorted_images = sorted(
            response['imageDetails'],
            key=lambda k: k['imagePushedAt'],
            reverse=True
        )

        # Retrieve the latest pushed image
        latest_image = sorted_images[0]

        # Process the latest image
        print('Latest image details:', latest_image)

        # Assuming the Lambda function receives electricity_price as an event parameter
        electricity_price = float(event.get('electricity_price', 0.0))

        # Create a Grid instance
        grid = Grid(electricity_price)

        # Call the get_Electricity_Price method of the Grid instance
        electricity_price = grid.get_Electricity_Price()
        print('BBBBBB')
        print('succesufullydone')

        return {
            'statusCode': 200,
            'body': 'Lambda function executed successfully.',
            'electricity_price': electricity_price
        }

    except Exception as e:
        print('Error:', str(e))
        return {
            'statusCode': 500,
            'body': 'An error occurred while processing the Lambda function.'
        }
