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

    client = CosmosClient(url, key,consistency_level="Session")
    try:
        client.create_database_if_not_exists(db)
    except:
        return func.HttpResponse(body="Database could not be deleted, does it exist?", status_code=200)
    return func.HttpResponse(body="Created Container", status_code=200)
