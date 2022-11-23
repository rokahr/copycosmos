import logging

import azure.functions as func
import json
from azure.cosmos import CosmosClient

def main(req: func.HttpRequest) -> func.HttpResponse:

    logging.info('Python HTTP trigger function processed a request.')

    url = req.params.get('url')
    key = req.params.get('key')
    db = req.params.get('db')

    client = CosmosClient(url, key,consistency_level="Session")
    database_name = db
    database = client.get_database_client(database=database_name)   
    containers = list(database.list_containers())

    return func.HttpResponse(body=json.dumps(containers), status_code=200)


