from flask import Flask, render_template, request, flash
from flask_bootstrap import Bootstrap
from flask_script import Manager
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Required

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
bootstrap = Bootstrap(app)
manager = Manager(app)


@app.route('/', methods=['POST', 'GET'])
def index():
    return 'hello, World!'

if __name__ == '__main__':
    app.run()
