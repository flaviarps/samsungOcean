import sqlite3
from flask import Flask, request, session, g, redirect, abort, render_template, flash

#configurações
DATABASE = "blog.db"
SECRET_KEY = "pudim"

app = Flask(__name__)
app.config.from_object(__name__)

def conectar_bd():
        return sqlite3.connect(app.config['DATABASE'])

@app.before_request
def antes_requesicao():
        g.bd = conectar_bd()

@app.teardown_request
def depois_requesicao(exc):
        g.bd.close()

@app.route('/')
def exibir_entradas():
        return render_template("exibir_entradas.html")

@app.route('/hello')
def pagina_inicial():
        return "Hello World"

# Instalar os módulos
# php install flask python-dotenv pyngrok

# Verificar módulos e dependências instaladas
# pip freeze

# Salvar em arquivo os módulos instalados
# pip freeze > requeriments.txt

# Para preparar outros ambientes com os memos módulos do projeto
# pip install -r requeriments.txt

# Criar o database
# sqlite3 blog.db < esquema.sql