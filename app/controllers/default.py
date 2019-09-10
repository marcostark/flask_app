from flask import render_template, flash, redirect, url_for
from app import app, db, lm

from app.models.forms import LoginForm

from app.models.tables import User
from flask_login import login_user, logout_user


@lm.user_loader
def load_user(id):
    # Usuario logado no momento
    return User.query.filter_by(id=id).first()

@app.route("/index")
@app.route("/")
def index():
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
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.password == form.password.data:
            login_user(user)
            return redirect(url_for("index"))
            flash("Logged in.")
        else:
            flash("Invalid login")
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

    #Select com filtro
    users = User.query.filter(username="stark").all()

    return "Ok"


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("login"))