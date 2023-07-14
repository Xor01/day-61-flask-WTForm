from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import PasswordField, SubmitField, validators, EmailField
from wtforms.validators import DataRequired
from flask_bootstrap import Bootstrap5
from os import getenv
from dotenv import load_dotenv


class LoginForm(FlaskForm):
    email = EmailField(label='email',
                       validators=[
                           DataRequired(), validators.Email()])
    password = PasswordField(label='password', validators=[DataRequired(), validators.length(min=8)])
    submit = SubmitField(label='Log in')


app = Flask(__name__)
app.secret_key = getenv('SECRET_KEY')
bootstrap = Bootstrap5(app=app)


@app.route("/")
def home():
    return render_template('index.html', bootstrap=bootstrap)


@app.route('/login.html', methods=['get', 'post'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        if login_form.email.data == 'admin@email.com' and login_form.password.data == '12345678':
            return render_template('success.html')
        return render_template('denied.html')
    return render_template('login.html', form=login_form)


if __name__ == '__main__':
    load_dotenv()
    app.run(debug=True)
