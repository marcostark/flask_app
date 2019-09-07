from flask import Flask


# Variavel que tem todo o controle da aplicacao
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
