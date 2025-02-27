from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('base.html')

@app.route('/index/<title>')
def index(title):
    return render_template('base.html', title=title)


@app.route('/promotion')
def promotion():
    return '''Человечество вырастает из детства.<br><br>
Человечеству мала одна планета.<br><br>
Мы сделаем обитаемыми безжизненные пока планеты.<br><br>
И начнем с Марса!<br><br>
Присоединяйся!<br><br>'''

@app.route('/image_mars')
def mars_picture():
    return render_template('image_mars.html')

@app.route('/promotion_image')
def promotion_image():
    return render_template('promotion.html')

@app.route('/training/<prof>')
def traning(prof):
    c =  {'prof': prof}
    return render_template('Training.html', **c)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)
