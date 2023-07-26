import boto3

# Table Name
table_name = 'Movies'

# dynamodb client
dynamodb_client = boto3.resource('dynamodb')

# item scarface movie
item_scarface = {
    'Title': {'S': 'Scarface'},
    'Year': {'S': '1983'}
}


if __name__ == "__main__":
    dynamodb_client.put_item(TableName=table_name, Item=item_scarface)