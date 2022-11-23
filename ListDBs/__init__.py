import logging

import azure.functions as func
import json
from azure.cosmos import CosmosClient

def main(req: func.HttpRequest) -> func.HttpResponse:

    logging.info('Python HTTP trigger function processed a request.')

    url = req.params.get('url')
    key = req.params.get('key')

    client = CosmosClient(url, key,consistency_level="Session")
    dbs_iter=client.list_databases()
    dbs = []
    for db in dbs_iter:
        dbs.append(db['id'])

    return func.HttpResponse(body=json.dumps(dbs), status_code=200)


