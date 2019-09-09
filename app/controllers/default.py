from flask import render_template
from app import app, db

from app.models.forms import LoginForm

from app.models.tables import User


@app.route("/index")
@app.route("/")
def hello_world():
    return render_template('index.html')


@app.route("/test", defaults={'name': None})
@app.route("/test/<name>")
def test(name):
    if name:
        return "Olá, %s !" % name
    else:
        return "Olá, usuário!"


@app.route("/login", methods=[ "GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        print(form.password.data)
    else:
        # Dicionario de erros
        form.errors
    return render_template('login.html',
                           form=form)


@app.route("/teste/<info>")
@app.route("/teste", defaults={"info": None})
def teste(info):
    i = User("stark", "1234","Marcos Stark", "mrcs.stark@gmail.com")
    db.session.add(i)
    db.session.commit()
    return "Ok"
