from flask import Blueprint, render_template, abort
from flask_login import login_required
from flask_security import current_user
from flask_security import auth_required
from jinja2 import TemplateNotFound
from werkzeug.utils import redirect

index = Blueprint('index', __name__, template_folder='templates')


@index.route("/", methods=["GET", "POST"])
# @auth_required()
@login_required
def show():
    # if not current_user.is_active:
    #     return redirect("login")
    # else:
        try:
            return render_template('index.html')
        except TemplateNotFound:
            abort(404)
