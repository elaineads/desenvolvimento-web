from flask import Flask
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'elaine'
app.config['MYSQL_DB'] = 'bd_unes'

mysql = MySQL(app)

from views import *

if __name__ == "__main__":
    app.run(debug=True)