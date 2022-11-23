import logging

import azure.functions as func
import json
from azure.cosmos import exceptions, CosmosClient, PartitionKey


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')


    req_body = req.get_json()
    url = req_body.get('url')
    key = req_body.get('key')
    db = req_body.get('db')
    container = req_body.get('container')

    client = CosmosClient(url, key,consistency_level="Session")
    database_name = db
    database = client.get_database_client(database=database_name)   
    
    database.delete_container(container=container)

    return func.HttpResponse(body="Deleted Container", status_code=200)
