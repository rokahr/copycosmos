import logging

import azure.functions as func
import json
from azure.cosmos import CosmosClient
import uuid

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
    container = database.get_container_client(container)

    with open('data/large-file.json', encoding='utf-8') as json_file:
        data = json.load(json_file)

    for line in data:
        line['id'] = str(uuid.uuid4())
        try:
            container.create_item(line)
            print('done')
        except:
            print('error')

    return func.HttpResponse(body='Uploaded', status_code=200)


