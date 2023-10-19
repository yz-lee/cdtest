import os
import flask
from flask import Flask, render_template, request
from flask_wtf.csrf import CSRFProtect

app = flask.Flask(__name__)
csrf = CSRFProtect(app)
app.config['SECRET_KEY'] = os.urandom(24)

@app.route("/myform")

def form():
    return render_template('myformcsrf.html')

@app.route("/submit", methods=['POST'])
def submit():
    account = request.values['account']
    password = request.values['password']
    if password == "Testtest":
        return render_template('resp.html', **locals())
    else:
        return "<H1> Error Account or Password! <H1>"

if __name__ == '__main__':
    app.run(host='0.0.0.0')
