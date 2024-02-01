from flask import Flask, render_template, request, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, validators


app = Flask(__name__)
app.config['SECRET_KEY'] = 'une_clé_secrète_très_difficile_à_déviner'
class RegistrationForm(FlaskForm):
    username = StringField('Username', [validators.Length(min=4, max=25)])
    email = StringField('Email Address', [validators.Length(min=6, max=35)])
    password = PasswordField('New Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        # Ici, le traitement des données validées
        return redirect(url_for('success'))
    return render_template('register.html', form=form)

@app.route('/success', methods=['GET'])
def success():
    return "OK"


if __name__ == "__main__":
    app.run(debug=True)
