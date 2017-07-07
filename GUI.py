from flask import Flask, jsonify, render_template, request, flash
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
    name = StringField('Title: ')
    author = StringField('author: ')
    submit = SubmitField('download')

def novel_download(jsonfile):
    novel = Novel(jsonfile)

    print(novel.info.get_title())
    print(novel.info.get_author())
    print(novel.info.get_url())

    novel.save()


def content_fix():
    Content().update()


class SettingForm(FlaskForm):
    name = StringField('Title: ', validators=[Required()])
    author = StringField('Author: ', validators=[])
    url = StringField('URL: ', validators=[Required()])
    submit = SubmitField('Save')


@app.route('/', methods=['POST', 'GET'])
def index():
    form = NovelForm()

    jsonfile = JsonFile()
    name = jsonfile.get_title()
    author = jsonfile.get_author()

    print("index: " + name)
    print("index: " + author)

    if request.method == 'POST':

        novel_download(jsonfile)
        content_fix()

    return render_template('index.html', form=form, name=name, author=author)


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
    if form.validate_on_submit() and request.method == 'POST':
        name = form.name.data
        author = form.author.data
        url = form.url.data

        print(name)
        print(author)
        print(url)

        json_setting(name, author, url)

        flash('設定成功!!')

    return render_template('setting.html', form=form, name=name, author=author, url=url)

if __name__ == '__main__':
    app.run(debug=True)
