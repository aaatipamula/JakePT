'''
Authors: Aniketh Aatipamula, Omar Mohammed
Purpose: Run the main Flask app
'''
from flask import Flask, render_template, request, redirect, url_for

app = Flask('JakePT')

from ai import create_chain
import api

def valid_currency(string: str) -> bool:
    string = string.replace("$", "")
    string = string.replace(".", "")
    string = string.replace(",", "")
    return string.isdecimal()

@app.route('/', methods=['GET','POST'])
def homepage():
    if request.method == 'GET':
        return render_template('info.html', error=False)

    name = request.form.get('name', '').strip().title()
    budget = request.form.get('budget', '').strip()

    if budget and not valid_currency(budget):
        return render_template('info.html', error=True)


    return redirect(url_for("jake") + "?name=" + name + "&budget=" + budget)

@app.get('/JakePT')
def jake():
    name = request.args.get('name')
    budget = request.args.get('budget')
    return render_template('chat.html', name=name, budget=budget)

@app.get('/chat')
def chat():
    name = request.args.get('name')
    budget = request.args.get('budget')
    question = request.args.get('question')

    if not(name and budget and question):
        return "No name, budget or question found"
    url = url_for('info_placeholder') + '?categories='
    chat = create_chain(url, request.args, ['hi'])
    response = chat.invoke({"question": question})
    return response.content
    
