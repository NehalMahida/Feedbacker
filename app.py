from flask import Flask, render_template, request, redirect
import os
from werkzeug.utils import secure_filename
from pdfRead import extractTable
from flaskext.mysql import MySQL
import csv
import json
from flask import jsonify

app = Flask(__name__)

mysql = MySQL()
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'facultyfeedback'
mysql.init_app(app)

db = mysql.connect()
cursor = db.cursor()


def addDetails(f_name, sub_code, sub_name, program_name, institute_name, dept_name, sem_name, aca_year, no_student, no_feed, filename):
    if program_name == '1':
        program_name = "Btech"
    else:
        program_name = "Mtech"
    if institute_name == '1':
        institute_name = "CSPIT"
    else:
        institute_name = "DEPSTAR"
    if dept_name == '1':
        dept_name = "CE"
    elif dept_name == '2':
        dept_name = "IT"
    else:
        dept_name = "CSE"
    print(filename)
    sql = "INSERT INTO response_master(Pdf_Id, Institute_Name, Dept_Name, Program, Academy_Year, Semester, Subject_Code, Subject_Name, Faculty_Name, q1, q2, q3, q4, q5, q6, q7,q8, q9, q10, q11, q12, q13, q14, q15, q16, q17, q18, q19, q20, q21, q22, q23, q24, q25, q26, q27, q28, q29, q30, q31, q32, q33, q34, q35, q36, q37, q38, q39, q40, q41, q42, q43, q44, q45, q46, q47, q48, q49, q50, q51,q52, q53, q54, q55, q56, q57, q58, q59, q60, Total_stu, Total_feed) VALUES(NULL, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    aca_year = int(aca_year)
    values = (institute_name, dept_name, program_name,
              aca_year, sem_name, sub_code, sub_name, f_name)
    with open('createFiles/' + filename + '.csv') as f:
        data = [tuple(line) for line in csv.reader(f)]
        data = data[0]
    data = list(data)
    for i in range(0, len(data)):
        data[i] = int(data[i])
    data = tuple(data)
    # print(data)
    values = values + data
    values = values + (no_student, no_feed)
    # print(values)
    cursor.execute(sql, values)
    db.commit()
    return


@app.route('/barchart')
def barchart():
    sql = "SELECT Faculty_Name, (q1+q6+q11+q16+q21+q26+q31+q36+q41+q46+q51+q56+q1+q6+q11+q16+q21+q26+q31+q36+q41+q46+q51+q56+q1+q6+q11+q16+q21+q26+q31+q36+q41+q46+q51+q56+q1+q6+q11+q16+q21+q26+q31+q36+q41+q46+q51+q56+q1+q6+q11+q16+q21+q26+q31+q36+q41+q46+q51+q56)/12 as A, (q2+q7+q12+q17+q22+q27+q32+q37+q42+q47+q52+q57+q2+q7+q12+q17+q22+q27+q32+q37+q42+q47+q52+q57+q2+q7+q12+q17+q22+q27+q32+q37+q42+q47+q52+q57+q2+q7+q12+q17+q22+q27+q32+q37+q42+q47+q52+q57+q2+q7+q12+q17+q22+q27+q32+q37+q42+q47+q52+q57)/12 as B, (q3+q8+q13+q18+q23+q28+q33+q38+q43+q48+q53+q58+q3+q8+q13+q18+q23+q28+q33+q38+q43+q48+q53+q58+q3+q8+q13+q18+q23+q28+q33+q38+q43+q48+q53+q58+q3+q8+q13+q18+q23+q28+q33+q38+q43+q48+q53+q58+q3+q8+q13+q18+q23+q28+q33+q38+q43+q48+q53+q58)/12 as C, (q4+q9+q14+q19+q24+q29+q34+q39+q44+q49+q54+q59+q4+q9+q14+q19+q24+q29+q34+q39+q44+q49+q54+q59+q4+q9+q14+q19+q24+q29+q34+q39+q44+q49+q54+q59+q4+q9+q14+q19+q24+q29+q34+q39+q44+q49+q54+q59+q4+q9+q14+q19+q24+q29+q34+q39+q44+q49+q54+q59)/12 as D, (q5+q10+q15+q20+q25+q30+q35+q40+q45+q50+q55+q60+q5+q10+q15+q20+q25+q30+q35+q40+q45+q50+q55+q60+q5+q10+q15+q20+q25+q30+q35+q40+q45+q50+q55+q60+q5+q10+q15+q20+q25+q30+q35+q40+q45+q50+q55+q60+q5+q10+q15+q20+q25+q30+q35+q40+q45+q50+q55+q60)/12 as E from response_master WHERE Subject_Code = 'CE341' AND Semester = 5 AND Academy_Year = 2020"
    cursor.execute(sql)
    rv = cursor.fetchall() 
    fname = []
    a = []
    b = []
    c = []
    d = []
    e = []
    for result in rv:
        fname.append(result[0]) 
        a.append(int(result[1]))
        b.append(int(result[2]))
        c.append(int(result[3]))
        d.append(int(result[4]))
        e.append(int(result[5]))
    '''payload = []
    content = {}
    for result in rv:
        content = {'id': result[0]}
        payload.append(content)
        content = {}'''
    data = {
        "FacultyName" : fname,
        "Excellent" : a,
        "Good" : b,
        "Average" : c,
        "Bad" : d,
        "VeryBad" : e
    }
    return data

@app.route('/tryc')
def tryc():
    return render_template('barChart.html')


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        f_name = request.form['f_name']
        sub_code = request.form['sub_code']
        sub_name = request.form['sub_name']
        program_name = request.form['program_name']
        institute_name = request.form['institute_name']
        dept_name = request.form['dept_name']
        sem_name = request.form['sem_name']
        aca_year = request.form['aca_year']
        no_student = request.form['no_student']
        no_feed = request.form['no_feed']
        up_pdf = request.files['up_pdf']        
        filename = secure_filename(up_pdf.filename)
        up_pdf.save(os.path.join('uploads', filename))
        extractTable('uploads/', filename)
        addDetails(f_name, sub_code, sub_name, program_name, institute_name,
                   dept_name, sem_name, aca_year, no_student, no_feed, filename)
        return render_template('barChart.html')
    else:
        return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
