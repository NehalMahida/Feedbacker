from flask import Flask, render_template, request, redirect
import os
from werkzeug.utils import secure_filename
from pdfRead import extractTable

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        f_name = request.form['f_name']        
        sub_code = request.form['sub_code']
        sub_name = request.form['sub_name']
        program_name = request.form['program_name']
        dept_name = request.form['dept_name']
        sem_name = request.form['sem_name']
        aca_year = request.form['aca_year']
        no_student = request.form['no_student']
        no_feed = request.form['no_feed']
        up_pdf = request.files['up_pdf']
        print(f_name)
        print(sub_code)
        print(sub_name)
        print(program_name)
        print(dept_name)
        print(sem_name)
        print(aca_year)
        print(no_feed)
        print(no_student)      
        #print(up_pdf) 
        filename = secure_filename(up_pdf.filename)
        up_pdf.save(os.path.join('uploads', filename))
        extractTable('uploads/'+filename)
        return redirect('/')
    else:
        return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)     