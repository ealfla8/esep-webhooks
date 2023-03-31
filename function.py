import json
import requests

def lambda_handler(event, context):
    # TODO implement
    message = "Issue Created: " + event['issue']['html_url']
    with open('secret.key') as file_input: 
        url = file_input.read().strip()
    r = requests.post(url, json = {"text": message})
    return r.text