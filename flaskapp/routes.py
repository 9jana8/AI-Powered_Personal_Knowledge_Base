from flask import render_template, url_for, redirect, flash
from flaskapp import app
from flaskapp.forms import RegistrationForm, LoginForm

posts = [
    {
        'author': 'Author One',
        'title': 'First Post',
        'content': 'This is the content of the first post.',
        'date_posted': 'April 20, 2024'},
    {
        'author': 'Author Two',
        'title': 'Second Post',
        'content': 'This is the content of the second post.',
        'date_posted': 'April 21, 2024'}
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == '9jana8@gmail.com' and form.password.data == 'password':
            flash('Login successful!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)