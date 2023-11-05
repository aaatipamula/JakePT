'''
Authors: Aniketh Aatipamula, Omar Mohammed
Purpose: Set up the API
'''
from main import app
from flask import requests
import json 

file = open('data.json')
database = json.load(file)



@app.get("/api/info")
def get_containers():
    keys = requests.args.get()
    keys_list = keys.split()
    for item in keys_list:
        if item in database:
            return item
