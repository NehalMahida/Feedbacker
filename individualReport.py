from flask import request
from flask import jsonify
from dbConnection import connection

import json



def getSubjectNames_indi(data):
    db, cursor = connection()
    sql = "SELECT sub_master.subjectName from faculty_master INNER JOIN sub_master on faculty_master.sub_id = sub_master.sub_id WHERE faculty_master.faculty_code = %s"
    cursor.execute(sql, data)
    resultSet = cursor.fetchall()
    faculty_name = []
    for result in resultSet:
        faculty_name.append(result[0])   
    cursor.close()  
    #print(faculty_name)
    return jsonify(faculty_name)

def showBarChart_indi(req):
    db, cursor = connection()
    sql = "SELECT `q1`, `q2`, `q3`, `q4`, `q5`, `q6`, `q7`, `q8`, `q9`, `q10`, `q11`, `q12`, `q13`, `q14`, `q15`, `q16`, `q17`, `q18`, `q19`, `q20`, `q21`, `q22`, `q23`, `q24`, `q25`, `q26`, `q27`, `q28`, `q29`, `q30`, `q31`, `q32`, `q33`, `q34`, `q35`, `q36`, `q37`, `q38`, `q39`, `q40`, `q41`, `q42`, `q43`, `q44`, `q45`, `q46`, `q47`, `q48`, `q49`, `q50`, `q51`, `q52`, `q53`, `q54`, `q55`, `q56`, `q57`, `q58`, `q59`, `q60` from response_master WHERE response_master.Faculty_Name = (SELECT faculty_master.faculty_name from faculty_master WHERE faculty_master.faculty_code = %s ) AND response_master.Subject_Name = %s"    
    req = json.loads(req)
    values = (req[0], req[1])
    cursor.execute(sql, values)
    resultSet = cursor.fetchall()
    print('resultset:', resultSet)
    questions = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    a = []
    b = []
    c = []
    d = []
    e = []
    for result in resultSet:
        for i in range(0, 60, 5):
            a.append(int(result[i]))
        for i in range(1, 60, 5):
            b.append(int(result[i]))
        for i in range(2, 60, 5):
            c.append(int(result[i]))
        for i in range(3, 60, 5):
            d.append(int(result[i]))
        for i in range(4, 60, 5):
            e.append(int(result[i]))
    data = {
        "Question No": questions,
        "Excellent": a,
        "Good": b,
        "Average": c,
        "Bad": d,
        "VeryBad": e
    }
    print(data)
    cursor.close()
    return data