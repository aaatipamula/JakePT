'''
Authors: Aniketh Aatipamula, Omar Mohammed
Purpose: Run the main Flask app
'''
from flask import Flask
app = Flask('JakePT')

import api

@app.get('/')
def render_homepage():
    pass
