from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE__URI"] = "sqlite:///mercado.db"
db.init_app(app)

@app.route('/')
def page_home():
    return render_template("home.html")

@app.route('/produtos')
def page_produtos():
    itens = [
        {'id':1, 'nome':'Celular', 'cod_barra':191991, 'preco':1200},
        {'id':2, 'nome':'Notbook', 'cod_barra':121345, 'preco':2300},
        {'id':3, 'nome':'teclado', 'cod_barra':191923, 'preco':250},
        {'id':4, 'nome':'monitor', 'cod_barra':201991, 'preco':600},
        {'id':5, 'nome':'mause', 'cod_barra':202012, 'preco':130}
    ]
    return render_template('produtos.html', itens=itens)