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
 # Retrieve the ECR repository and image details from the event
    repository_name = event['detail']['repository-name']
    image_digest = event['detail']['image-digest']

    lambda_client = boto3.client('lambda')
    function_name = 'lambdatryascontainer'  # Replace with your Lambda function name

    latest_version = get_latest_lambda_version(lambda_client, function_name)
    update_lambda_function_code(lambda_client, function_name, latest_version, repository_name, image_digest)

    # Rest of your existing code
    # Assuming the Lambda function receives electricity_price as an event parameter
    electricity_price = float(event.get('electricity_price', 0.0))

    # Create a Grid instance
    grid = Grid(electricity_price)
    print('trythis verison ')

    # Call the get_Electricity_Price method of the Grid instance
    electricity_price = grid.get_Electricity_Price()
    print('BBBBBB')

def get_latest_lambda_version(lambda_client, function_name):
    response = lambda_client.list_versions_by_function(FunctionName=function_name)
    versions = response['Versions']
    latest_version = max(versions, key=lambda v: int(v['Version']))
    return latest_version['Version']

def update_lambda_function_code(lambda_client, function_name, latest_version, repository_name, image_digest):
    new_image_uri = f'{repository_name}@{image_digest}'

    response = lambda_client.update_function_code(
        FunctionName=function_name,
        ImageUri=new_image_uri,
        Publish=True
    )

    print(f"Lambda function {function_name} updated with the latest image: {new_image_uri}")
