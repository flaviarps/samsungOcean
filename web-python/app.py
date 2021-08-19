import sqlite3
from flask import Flask, request, session, g, redirect, abort, render_template, flash

#configurações
DATABASE = "blog.db"
SECRET_KEY = "pudim"

app = Flask(__name__)
app.config.from_object(__name__)

@app.route('/hello')

def conectar_bd():
        return sqlite3.connect(app.config['DATABASE'])

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