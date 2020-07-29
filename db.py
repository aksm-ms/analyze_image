import uuid
from azure.cosmos import exceptions, CosmosClient, PartitionKey


def initialize():
    endpoint = "<cosmos db endpoint>"
    key = '<db key>'
    client = CosmosClient(endpoint, key)

    database_name = 'image-data'
    print("database name: " + database_name)
    database = client.create_database_if_not_exists(id=database_name)

    container_name = 'image-analyze-data'
    print("container name: " + container_name)
    container = database.create_container_if_not_exists(
        id=container_name,
        partition_key=PartitionKey(path="/requestId"),
        offer_throughput=400
    )
    return container


def write_to_db(data):
    container = initialize()
    uniq_id = str(uuid.uuid4())
    data['id'] = uniq_id
    print("db id is: " + uniq_id)
    container.create_item(body=data)
    print("item created in db!")
