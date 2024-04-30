from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, SelectField, TextAreaField
from wtforms.validators import DataRequired, Email
from models.task import TaskStatus, PriorityLevel


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')


class RegisterForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Confirm Password', validators=[DataRequired()])
    submit = SubmitField('Register')


class ProjectForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    description = TextAreaField('Description')
    submit = SubmitField('Create Project')


def status_choices():
    return [
        (choice.name, choice.name.replace("_", " ").title()) for choice in TaskStatus
    ]


def priority_choices():
    return [(choice.name, choice.name.capitalize()) for choice in PriorityLevel]


class TaskForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    description = TextAreaField('Description')
    status = SelectField(
        'Status', choices=status_choices(), coerce=str, validators=[DataRequired()]
    )
    priority = SelectField(
        'Priority', choices=priority_choices(), coerce=str, validators=[DataRequired()]
    )
    submit = SubmitField('Add Task')
