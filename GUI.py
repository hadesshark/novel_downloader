from flask import Flask, render_template, request, flash
from flask_bootstrap import Bootstrap
from flask_script import Manager
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Required

from downloader import Novel, SettingInfo
from content_fix import Content

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
bootstrap = Bootstrap(app)
manager = Manager(app)


class NovelForm(FlaskForm):
    name = StringField('Title: ')
    author = StringField('author: ')
    url = StringField('URL: ')
    submit = SubmitField('download')


def novel_download(jsonfile):
    novel = Novel(jsonfile)
    novel.save()


def content_fix():
    Content().update()


class SettingForm(FlaskForm):
    name = StringField('Title: ', validators=[Required()])
    author = StringField('Author: ', validators=[])
    url = StringField('URL: ', validators=[Required()])
    submit = SubmitField('Save')


class JsonFile(SettingInfo):

    def get_info(self):
        return (self.get_title(), self.get_author(), self.get_url())

    def set_info(self, name, author, url):
        self.set_title(name)
        self.set_url(url)
        self.set_author(author)


class Data(object):
    def __init__(self, form, name, author, url):
        self.form = form
        self.name = name
        self.author = author
        self.url = url


@app.route('/', methods=['POST', 'GET'])
def index():
    form = NovelForm()

    name, author, url = JsonFile().get_info()

    if request.method == 'POST':
        novel_download(JsonFile())  # 這樣寫不太好，需要改
        content_fix()
        flash('下載完成！！')

    data = Data(form, name, author, url)
    return render_template('index.html', data=data)


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

    data = Data(form, name, author, url)

    return render_template('setting.html', data=data)


@app.route('/convert')
def convert():
    print("成功！！")

if __name__ == '__main__':
    manager.run()
