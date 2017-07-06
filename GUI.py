from flask import Flask, jsonify, render_template, request
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Required

from downloader import Novel
from initialize import JsonFile
from content_fix import Content

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
bootstrap = Bootstrap(app)
moment = Moment(app)


def reset_name():
    return JsonFile().get_title()

def reset_author():
    return JsonFile().get_author()


class NovelForm(FlaskForm):
    name = StringField('Title: ' + reset_name())
    author = StringField('author: ' + reset_author())
    submit = SubmitField('download')

def novel_download():
    Novel().save()


def content_fix():
    Content().update()


class SettingForm(FlaskForm):
    name = StringField('Title: ', validators=[Required()])
    author = StringField('Author: ', validators=[])
    url = StringField('URL: ', validators=[Required()])
    submit = SubmitField('Save')


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        novel_download()
        content_fix()
    form = NovelForm()
    return render_template('index.html', form=form)


def json_setting(name, author, url):
    jsonfile = JsonFile()
    jsonfile.set_title(name)
    jsonfile.set_url(url)
    jsonfile.set_author(author)

@app.route('/setting', methods=['POST', 'GET'])
def setting():
    name = None
    author = None
    url = None

    form = SettingForm()
    if form.validate_on_submit():
        print("yessssss")
        name = form.name.data
        author = form.author.data
        url = form.url.data

        json_setting(name, author, url)

    else:
        print("nooooo")

    return render_template('setting.html', form=form, name=name, author=author, url=url)

if __name__ == '__main__':
    app.run()
