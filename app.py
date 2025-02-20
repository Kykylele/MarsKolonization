from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Миссия Колонизация Марса</h2>'


@app.route('/index')
def mission():
    return '<h2>И на Марсе будут яблони цвести!</h2>'


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)
