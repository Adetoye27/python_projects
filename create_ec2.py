'''
Write a function to create an EC2 instance with the name ec2-created-by-python.
Use all the best practices, handle exception, use variables, use main, doc strings etc…
'''

import boto3
import logging

# setup logger
# FORMAT = '%(asctime)s %(clientip)-15s %(user)-8s %(message)s'
logging.basicConfig(filename='myapp.log', level=logging.INFO,format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S')
logger = logging.getLogger(__name__)

def create_ec2(instance_type='t3.micro', image_id='ami-0aa7d40eeae50c9a9',subnet_id='subnet-0435cec4a109231cf'): 
    '''
    create an EC2 instance with the name ec2-created-by-python

    Parameters:
    - Instance Type : str
    - image_id : str
    - subnet_id: str

    Returns:
    - Dict: Reponse with the EC2 created info
    '''


    # Initialize the ec2 client
    ec2 = boto3.client('ec2')
    
    try:
        response = ec2.run_instances(
            InstanceType = instance_type, 
            ImageId = image_id,
            SubnetId = subnet_id,
            MaxCount = 1,
            MinCount = 1,
            TagSpecifications=[
                {
                    'ResourceType':'instance',
                    'Tags': [
                        {
                            'Key': 'Name',
                            'Value': 'ec2-created-by-python'
                        }
                    ]
                }
            ]
        )
        logger.info(f"EC2 instance with InstanceType {instance_type} and Amazon ami ID {image_id} is created  ")
        return response

    except Exception as e:
        logger.error(f"Error creating EC2 instance: {str(e)}")
    
# main
if __name__ == "__main__":
    create_ec2()
    logger.info(f"The ec2 was created successfully")


                
             
            





