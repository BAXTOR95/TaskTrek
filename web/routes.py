from flask import Blueprint, render_template, request, redirect, url_for, flash
from models import Task, Project, User
from models.database import db
from web.forms import LoginForm, RegisterForm
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.exc import IntegrityError
from flask_login import login_user, login_required, logout_user, current_user
from datetime import datetime, UTC
from web.utils.gravatar import gravatar_url

web_blueprint = Blueprint('web', __name__, template_folder='templates')


@web_blueprint.app_context_processor
def inject_content():
    """Injects the current year into all templates."""
    year = datetime.now().year
    return dict(year=year, gravatar_url=gravatar_url)


@web_blueprint.route("/")
def landing():
    """Displays the landing page with a prompt to login or register."""
    if current_user.is_authenticated:
        return redirect(url_for("web.projects"))
    else:
        return render_template("landing.html")


@web_blueprint.route("/login", methods=["GET", "POST"])
def login():
    """Handles user login.

    GET: Displays the login form.
    POST: Processes the submitted form. Logs in the user if validation succeeds and the email and password match.
    Redirects to the dashboard page upon successful login or back to the login form with validation errors.

    Returns:
        Response: The login template on GET or redirect on successful POST.
    """
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        user = db.session.query(User).filter_by(email=email).first()
        if user and check_password_hash(user.password, password):
            login_user(user)
            user.last_login = datetime.now(UTC)
            db.session.commit()
            return redirect(url_for("web.projects"))
        else:
            flash("Invalid email or password", "danger")
    return render_template("login.html", form=form)


@web_blueprint.route("/register", methods=["GET", "POST"])
def register():
    """Handles user registration.

    GET: Displays the registration form.
    POST: Processes the submitted form. Registers a new user if validation succeeds and the email is not already taken.
    Redirects to the dashboard page upon successful registration or back to the register form with validation errors.

    Returns:
        Response: The register template on GET or redirect on successful POST.
    """
    form = RegisterForm()
    if form.validate_on_submit():
        try:
            email = form.email.data
            name = form.name.data
            password = form.password.data
            password2 = form.password2.data
            if password != password2:
                flash("Passwords do not match", "danger")
                return redirect(url_for("web.register"))
            hashed_password = generate_password_hash(
                password, method="pbkdf2:sha256", salt_length=8
            )
            new_user = User(
                email=email,
                name=name,
                password=hashed_password,
                last_login=datetime.now(UTC),
            )
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user)
            return redirect(url_for("web.projects"))
        except IntegrityError:
            db.session.rollback()
            flash("That email already exists, please login.", category="error")
            return redirect(url_for("web.login"))
    return render_template("register.html", form=form)


@web_blueprint.route('/logout')
@login_required
def logout():
    """Logs out the current user and redirects to the login page.

    Returns:
        Response: Redirect to the login page.
    """
    logout_user()
    flash("You have been logged out.", category='success')
    return redirect(url_for('web.login'))


@web_blueprint.route("/dashboard/projects")
@login_required
def projects():
    """Displays the user's projects on the dashboard."""
    user_projects = Project.query.filter_by(owner_id=current_user.id).all()
    projects = [project for project in user_projects]
    return render_template("projects.html", projects=projects)
