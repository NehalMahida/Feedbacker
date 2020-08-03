from flask import Flask
from flaskext.mysql import MySQL

def connection():
        app = Flask(__name__)
        mysql = MySQL()
        app.config['MYSQL_DATABASE_HOST'] = 'localhost'
        app.config['MYSQL_DATABASE_USER'] = 'root'
        app.config['MYSQL_DATABASE_PASSWORD'] = ''
        app.config['MYSQL_DATABASE_DB'] = 'facultyfeedback'
        mysql.init_app(app)
        db = mysql.connect()
        cursor = db.cursor()
        return db, cursor
