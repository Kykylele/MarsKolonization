from flask import Flask, render_template, request, make_response, session
from flask_wtf import FlaskForm
from werkzeug.utils import redirect
from wtforms import StringField, PasswordField, SubmitField, EmailField, BooleanField
from wtforms.validators import DataRequired
from data import db_session
from data.jobs import Jobs
from data.users import User
import datetime
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from flask_restful import Api
from users_resource import UsersResource, UsersListResource

app = Flask(__name__)
app.config['SECRET_KEY'] = 'gachimuchi'
login_manager = LoginManager()
login_manager.init_app(app)
api = Api(app)
api.add_resourse(UsersResource, '/api/v2/users/<int:user_id>')
api.add_resourse(UsersResource, '/api/v2/users')


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


class LoginForm(FlaskForm):
    email = EmailField('Почта', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')


class Jobsform(FlaskForm):
    title = StringField('Название работы')
    team_leader = StringField('ID сановника')
    work_size = StringField("Длительность работы")
    collaborators = StringField('Участники')
    finished = BooleanField('Завершена')
    submit = SubmitField('Добавить')


@app.route('/')
def main():
    session = db_session.create_session()
    jobs = session.query(Jobs).all()
    return render_template('index.html', jobs=jobs)


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
    c = {'prof': prof}
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
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        return render_template('login.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")


@app.route("/cookie_test")
def cookie_test():
    visits_count = int(request.cookies.get("visits_count", 0))
    if visits_count:
        res = make_response(
            f"Вы пришли на эту страницу {visits_count + 1} раз")
        res.set_cookie("visits_count", str(visits_count + 1),
                       max_age=60 * 60 * 24 * 365 * 2)
    else:
        res = make_response(
            "Вы пришли на эту страницу в первый раз за последние 2 года")
        res.set_cookie("visits_count", '1',
                       max_age=60 * 60 * 24 * 365 * 2)
    return res


app = Flask(__name__)
app.config['PERMANENT_SESSION_LIFETIME'] = datetime.timedelta(
    days=365
)


@app.route("/session_test")
def session_test():
    visits_count = session.get('visits_count', 0)
    session['visits_count'] = visits_count + 1
    return make_response(
        f"Вы пришли на эту страницу {visits_count + 1} раз")


@app.route('/jobs',  methods=['GET', 'POST'])
@login_required
def add_news():
    form = Jobsform()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        job = Jobs()
        job.job = form.title.data
        job.team_leader = form.team_leader.data
        job.work_size = form.work_size.data
        job.collaborators = form.collaborators.data
        job.is_finished = form.finished.data
        current_user.jobs.append(job)
        db_sess.merge(current_user)
        db_sess.commit()
        return redirect('/')
    return render_template('jobs.html', form=form)


if __name__ == '__main__':
    db_session.global_init('database/mars_explorer.db')
    app.run(host='127.0.0.1', port=8080)
