from datetime import timedelta

from flask import Flask, render_template, url_for, flash, redirect, session, request
from markupsafe import escape
from selenium import webdriver

from forms import RegistrationForm, LoginForm, CodeForm
import Driver
from PasswordReset import PasswordReset

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'

posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/trying")
def trying():
    if 'username' in session and 'email' in session and 'phoneNum' in session:
        username = escape(session['username'])  # getting username&email from the session
        email = escape(session['email'])
        phoneNum = escape(session['phoneNum'])
        # Here comes the code of reseting his password without he knows etc (Selenium)
        Driver.Initialize()
        PasswordReset.connect_to_site(phoneNum)
        return redirect(url_for('code'))
    return render_template('error.html')


@app.route("/code", methods=['GET', 'POST'])
def code():
    form = CodeForm()
    if form.validate_on_submit() and 'phoneNum' in session:
        phone_num = escape(session['phoneNum'])
        email = escape(session['email'])
        username = escape(session['username'])
        code_from_user = form.code.data
        PasswordReset.reset_password(code_from_user, phone_num)
        flash('Account created, ' + username + '!', 'success')
        return redirect(url_for('home'))
    return render_template('code.html', form=form)


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        session.permanent = True
        app.permanent_session_lifetime = timedelta(minutes=10)  # session for 10 min
        session['username'] = form.username.data  # saving username&email in session (using cookies)
        session['email'] = form.email.data
        session['phoneNum'] = form.phoneNum.data
        return redirect(url_for('trying'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)

if __name__ == '__main__':
    app.run(debug=True)
