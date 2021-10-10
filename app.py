# import os
# import magic
# import urllib.request
import glob
import warnings
# from app import app
from flask import (Flask, session, flash, redirect,
                   render_template, request, url_for, send_from_directory)
# from werkzeug.utils import secure_filename

import screen

warnings.filterwarnings(action='ignore', category=UserWarning, module='gensim')

app = Flask(__name__)

app.config.from_object(__name__)

# Load default config and override config from an environment variable
app.config.update(dict(
    USERNAME='admin ',
    PASSWORD='root',
    SECRET_KEY='root',
))

app.config['UPLOAD_FOLDER'] = 'Original_Resumes/'
app.config['ALLOWED_EXTENSIONS'] = {'txt', 'pdf', 'png', 'jpg', 'jpeg'}


class jd:
    def __init__(self, name):
        self.name = name


def getfilepath(loc):
    temp = str(loc).split('\\')
    return temp[-1]


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        session['logged_in'] = True
        flash('You were logged in')
        return redirect(url_for('home'))
    return render_template('login.html', error=error)


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('home'))


# @app.route('/')
# def upload_form():
#    return render_template('upload.html')


# ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])


# def allowed_file(filename):
#    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


# @app.route('/', methods=['POST'])
# def upload_file():
# if request.method == 'POST':
# check if the post request has the files part
# if 'files[]' not in request.files:
#   flash('No file part')
#   return redirect(request.url)
# files = request.files.getlist('files[]')
# for file in files:
# if file and allowed_file(file.filename):
#    filename = secure_filename(file.filename)
#    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
# flash('File(s) successfully uploaded')
# return redirect('/')


@app.route('/')
def home():
    x = []
    for file in glob.glob("./Job_Description/*.txt"):
        res = jd(file)
        x.append(jd(getfilepath(file)))
    print(x)
    return render_template('index.html', results=x)


@app.route('/results', methods=['GET', 'POST'])
def res():
    if request.method == 'POST':
        jobfile = request.form['des']
        print(jobfile)
        flask_return = screen.res(jobfile)

        print(flask_return)
        return render_template('result.html', results=flask_return)


# @app.route('/Original_Resumes/<path:filename>')
# def custom_static(filename):
#   return send_from_directory('./Original_Resumes', filename)


@app.route('/Original_Resumes/<path:filename>')
def custom_static(filename):
    return send_from_directory('./Resumes', filename)


# @app.route('/textresume/<path:filename>')
# def custom_static(report):
#    return send_from_directory('./Original_Resumes', report)


if __name__ == '__main__':
    # app.run(debug = True)
    app.run('localhost', 8000, debug=True, threaded=True)
