'''
Authors: Aniketh Aatipamula, Omar Mohammed
Purpose: Set up the API
'''

from main import app
from flask import request, jsonify 
import json 

file = open('data.json')
database = json.load(file)

@app.get("/api/info")
def get_containers():
    #receives the category keys 
    keys = request.args.get('keys', '')
    #receives the budget value 
    budget = request.args.get('budget')
    #turns the category keys into a list 
    keys_list = keys.split(',')
    #for every category, check if it is in the database dict, if not return an error
    guhpuht= []
    for item in keys_list:
        if item not in database:
            return jsonify({'error':'category does not exist in database'}),404
        else:
            category_opt = database.get(item) #pulls the dict associated to that category key 
            prices_cat = category_opt.get("prices")#pulls the dict that carries all the price category keys
            prices_keys = prices_cat.split()
            budget_range = min(prices_keys,key=lambda x: abs(x-budget))
            out = [category_opt[str(budget_range)],category_opt['claims'],category_opt['policies']]
            guhpuht.append(out)
    return str(guhpuht)

    
