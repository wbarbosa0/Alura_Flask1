from flask import Flask
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config.from_pyfile('config.py')

db = MySQL(app)

# Este import PRECISA estar aqui e não junto com os demais
# app precisa ter sido criado ANTES do import
from views import *

# Temos que ter essa condição
# para que não se saia executando a app durante os imports!!!
if __name__ == '__main__':
    app.run(debug=True)

