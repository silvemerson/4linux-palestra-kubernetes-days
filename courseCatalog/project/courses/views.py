from functools import wraps
from flask import request, redirect, flash,render_template, session, url_for, Blueprint
from project.models import Courses


courses_blueprint = Blueprint("courses",__name__)


def login_required(endpoint):
    @wraps(endpoint)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return endpoint(*args, **kwargs)
        else:
            flash('Necessário o login!!!')
            return(redirect(url_for('users.login')))
    return wrap


@courses_blueprint.route('/courses', methods=['GET'])
@login_required
def courses():
    courses = Courses.query.all()
    return render_template('listCourses.html',username=session['name'],courses=courses)
