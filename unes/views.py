from flask import Flask, render_template, request, redirect, url_for
from app import app, mysql
import config

@app.route("/")
def index():
    return render_template("index.html", title='UNES')

@app.route("/quem-somos")
def quemSomos():
    return render_template("quem-somos.html", title='Quem Somos')

@app.route("/contato")
def contato():
    return render_template("contato.html", title='Contato')

@app.route("/novo-contato", methods=['POST'])
def novoContato():
    if request.method == "POST":
        email = request.form['email']
        assunto = request.form['assunto']
        descricao = request.form['descricao']

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO contato (email, assunto, descricao) VALUES (%s, %s, %s)", (email, assunto, descricao))
        mysql.connection.commit()
        return redirect(url_for('mensagens'))

@app.route("/mensagens")
def mensagens():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM contato")
    data = cur.fetchall()
    cur.close()
    return render_template('mensagens.html', title='Mensagens', contato = data)