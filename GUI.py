from flask import Flask, render_template, request, flash
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_script import Manager
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
manager = Manager(app)


def reset_name():
    return JsonFile().get_title()


def reset_author():
    return JsonFile().get_author()


class NovelForm(FlaskForm):
    name = StringField('Title: ')
    author = StringField('author: ')
    url = StringField('URL: ')
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


class JsonFile(JsonFile):

    def get_info(self):
        return (self.get_title(), self.get_author(), self.get_url())

    def set_info(self, name, author, url):
        self.set_title(name)
        self.set_url(url)
        self.set_author(author)


def data(self, form, name, author, url):
    return form, name, author, url


@app.route('/', methods=['POST', 'GET'])
def index():
    form = NovelForm()

    name, author, url = JsonFile().get_info()

    if request.method == 'POST':
        novel_download(JsonFile())  # 這樣寫不太好，需要改
        content_fix()

    return render_template('index.html', form=form, name=name, author=author, url=url)


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

        JsonFile().set_info(name, author, url)

        flash('設定成功!!')

    return render_template('setting.html', form=form, name=name, author=author, url=url)

if __name__ == '__main__':
    manager.run()
