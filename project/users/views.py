from flask import redirect , render_template, request, session, flash, url_for, Blueprint
from .forms import LoginForm, RegisterForm
#from project import engine, Base
from project.models import Users
#from sqlalchemy.orm import scoped_session,sessionmaker
from project import db
from sqlalchemy.exc import IntegrityError
from functools import wraps


users_blueprint = Blueprint("users", __name__)

#def dbSession():
#    Base.metadata.bind = engine
#    DBSession = scoped_session(sessionmaker(bind=engine))
#    return DBSession

def login_required(endpoint):
    @wraps(endpoint)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return endpoint(*args, **kwargs)
        else:
            flash('Necessário o login!!!')
            return(redirect(url_for('users.login')))
    return wrap


@users_blueprint.route('/', methods=['GET','POST'])
def login():
    error = None
    form = LoginForm(request.form)

    if request.method == 'POST':
        if form.validate_on_submit():
            #db_session = dbSession()
            #user = db_session.query(Users).filter_by(name=request.form['name']).first()
            user = Users.query.filter_by(name=request.form['name']).first()
            if user is not None and user.password == request.form['password']:
                session['logged_in'] = True
                session['user_id'] = user.id
                session['role'] = user.role
                session['name'] = user.name
                flash('Bem vindo ao Painel de Cursos!!!')
                return redirect(url_for('courses.courses'))
            else:
                error = "Usuário ou senha errada!!!"

    return render_template('login.html', form=form, error=error)


@users_blueprint.route('/logout',methods=['GET'])
@login_required
def logout():
    session.pop('logged_in',None)
    session.pop('user_id',None)
    session.pop('role',None)
    session.pop('name',None)
    return redirect(url_for('users.login'))

@users_blueprint.route("/register", methods=['GET','POST'])
def register():
    error = None
    form = RegisterForm(request.form)

    if request.method == 'POST':
        if form.validate_on_submit():
            new_user = Users(
                request.form['name'],
                request.form['email'],
                request.form['password'],
                request.form['confirm'])
            print(request.form['name'])
            try:
                db.session.add(new_user)
                db.session.commit()
                flash('Obrigado por se registrar!!!')
                return redirect(url_for('users.login'))
            except IntegrityError:
                error = 'Esse usuário ou email já foram registrados'
                return render_template('register.html', form=form, error=error)
    return render_template('register.html', form=form, error=error)
