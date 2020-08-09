from flask import Flask, render_template, request, redirect
from werkzeug.utils import secure_filename
from flask import jsonify

from registerEntry import addEntry
from reportGenerate import showBarChart, showPieChart, getSubjectNames, getFacultyNames

import json
import os

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        req = request.form
        print(req)
        return render_template("index.html")
    else:
        return render_template("index.html")

@app.route('/getPieChart/<data>')
def getPieChart(data):
    #print(data)
    return showPieChart(data)

@app.route('/getBarChart/<data>')
def getBarChart(data):
    #print('bar chart')
    return showBarChart(data)


@app.route('/toRegister', methods=['POST', 'GET'])
def gotoRegister():
    if request.method == 'POST':
        # req object will have all the form values.
        req = request.form
        pdf_up = request.files['pdfUpload']
        filename = secure_filename(pdf_up.filename)
        pdf_up.save(os.path.join('uploads', filename))
        # addEntry is method os registerEntry.py file
        addEntry(req, filename)          
        return render_template('register.html')
    else:
        return render_template('register.html')

@app.route('/get_subject/<data>')
def get_subject(data):
    #print(data)
    return getSubjectNames(data)

@app.route('/get_faculty/<data>')
def get_faculty(data):    
    return getFacultyNames(data)

if __name__ == '__main__':
    app.run(debug=True)
