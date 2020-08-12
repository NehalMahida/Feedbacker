from flask import request
from flask import jsonify
from dbConnection import connection

import json



def showPieChart(req):
    #print('req : ', req)    
    percent = "SELECT Faculty_Name, Total_feed/Total_stu*100 as PER from response_master where Semester = %s and Dept_Name = %s and Subject_Name = %s ORDER by PER DESC"
    req = json.loads(req)
    values = (req[0], req[1], req[2])
    #print(values)
    db, cursor = connection()
    cursor.execute(percent, values)
    resultSet = cursor.fetchall()    
    f_name = []
    per = []
    for result in resultSet:
        f_name.append(result[0])
        per.append(int(result[1]))
    data = {
        'FacultyName' : f_name, 
        'Overall Feedback (%)' : per
    }    
    #print('query : ', data)
    cursor.close()
    return data

def showBarChart(req):    
    #print(req)
    sql = "SELECT Faculty_Name, (q1+q6+q11+q16+q21+q26+q31+q36+q41+q46+q51+q56)/12 as A, (q2+q7+q12+q17+q22+q27+q32+q37+q42+q47+q52+q57)/12 as B, (q3+q8+q13+q18+q23+q28+q33+q38+q43+q48+q53+q58)/12 as C, (q4+q9+q14+q19+q24+q29+q34+q39+q44+q49+q54+q59)/12 as D, (q5+q10+q15+q20+q25+q30+q35+q40+q45+q50+q55+q60)/12 as E from response_master WHERE  Semester = %s and Dept_Name = %s and Subject_Name = %s ORDER BY A DESC"
    req = json.loads(req)
    values = (req[0], req[1], req[2])
    db, cursor = connection()
    cursor.execute(sql, values)
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
    payload = []
    content = {}
    for result in rv:
        content = {'id': result[0]}
        payload.append(content)
        content = {}
    data = {
        "FacultyName": fname,
        "Excellent": a,
        "Good": b,
        "Average": c,
        "Bad": d,
        "VeryBad": e
    }
    #print('data ', data)
    cursor.close()
    return data

def getSubjectNames(sem):
    sql = "SELECT DISTINCT Subject_Name from response_master where Semester = %s and Dept_Name = %s"
    sem = sem.split(',')
    if sem[0]=='' or sem[1]=='':
        return jsonify([])
    values = (sem[0], sem[1]) 
    db, cursor = connection()     
    cursor.execute(sql, values)
    resultSet = cursor.fetchall()
    semester = []
    for result in resultSet:
        semester.append(result[0])   
    cursor.close()  
    return jsonify(semester)

def getFacultyNames(subject):   
    sql = "SELECT DISTINCT Faculty_Name from response_master where Semester = %s and Dept_Name = %s and Subject_Name = %s"
    subject = json.loads(subject)
    values = (subject[0], subject[1], subject[2])    
    db, cursor = connection()
    cursor.execute(sql, values)
    resultSet = cursor.fetchall()
    faculty = []
    for result in resultSet:
        faculty.append(result[0])    
    cursor.close()   
    return jsonify(faculty)
