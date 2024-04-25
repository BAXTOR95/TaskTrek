import os
from flask import Blueprint, render_template, request, redirect, url_for, flash
from models import Task, Project, User
from models.database import db
from web.forms import LoginForm, RegisterForm
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.exc import IntegrityError
from flask_login import login_user, login_required, logout_user


web_blueprint = Blueprint('web', __name__, template_folder='templates')


@web_blueprint.route("/")
def landing():
    """Displays the landing page with a prompt to login or register."""
    return render_template("landing.html")
