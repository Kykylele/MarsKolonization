from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from werkzeug.utils import redirect
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'gachimuchi'


class LoginForm(FlaskForm):
    astronautid = StringField('ID астронавта', validators=[DataRequired()])
    astronautpassword = PasswordField("Пароль астронавта", validators=[DataRequired()])
    cap_id = StringField('ID капитана', validators=[DataRequired()])
    cap_password = PasswordField("Пароль капитана", validators=[DataRequired()])
    access = SubmitField('Доступ')


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

@app.route('/list_prof/<lst>')
def prof(lst):
    c = {'list': lst, 'profs': ['Инженер изследовател', 'пилот', 'строител', 'екзобиолог', 'лекар', 'инженер по тераформиране']}
    return render_template('listprof.html', **c)

@app.route('/astronaut_selection')
def astro_sel():
    return render_template('asronaut_selection.html')

@app.route('/answer', methods=['POST'])
@app.route('/auto_answer', methods=['POST'])
def answer():
    context = {'title': 'Анкета', 'sur': request.form['surname'], 'name': request.form['name'], 'education': request.form['education'],
               'profession': ', '.join(request.form.getlist('profession')), 'motivation': request.form['motivation'],
               'ready': request.form.get('ready', '') == 'Готов'}
    return render_template('answer.html', **context)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'GET':
        return render_template('login.html', form=form)
    elif request.method == 'POST':
        if form.validate_on_submit():
            return redirect('/')

@app.route('/choice/<planet_name>')
def choise():
    return render_template('choise.html')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)
