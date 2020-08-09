from flask import request
from dbConnection import connection
from pdfRead import extractTable

import pandas



def addEntry(req, filename): 
    db, cursor = connection()   
    sql = "INSERT INTO response_master(Pdf_Id, Institute_Name, Dept_Name, Program, Academy_Year, Semester, Subject_Code, Subject_Name, Faculty_Name, q1, q2, q3, q4, q5, q6, q7,q8, q9, q10, q11, q12, q13, q14, q15, q16, q17, q18, q19, q20, q21, q22, q23, q24, q25, q26, q27, q28, q29, q30, q31, q32, q33, q34, q35, q36, q37, q38, q39, q40, q41, q42, q43, q44, q45, q46, q47, q48, q49, q50, q51,q52, q53, q54, q55, q56, q57, q58, q59, q60, Total_stu, Total_feed) VALUES(NULL, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"    
    values = (req['inputInstitute'], req['inputDepartment'], req['inputProgram'],
              req['inputAcademicYear'], req['inputSemester'], req['inputSubjectId'], req['inputSubjectName'], req['inputFacultyName'])         
    df = extractTable('uploads/', filename)
    tp = list(df.itertuples(index=False, name=None))[0]
    values = values + tp
    values = values + (req['inputTotalStudents'], req['inputTotalFeedback'])
    cursor.execute(sql, values)
    db.commit()
    cursor.close()