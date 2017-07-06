from flask import Flask, jsonify, render_template, request
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Required

from downloader import Novel
from initialize import JsonFile

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
bootstrap = Bootstrap(app)
moment = Moment(app)


class NovelForm(FlaskForm):
    name = StringField('file name: ' + JsonFile().__str__())
    submit = SubmitField('download')

@app.route('/novel_download')
def novel_download():
    Novel().save()


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        novel_download()
    form = NovelForm()
    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run()