import flask
from flask import Flask, render_template, send_file

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/downloaded') # this is a job for GET, not POST
def download_zip():
    return send_file(
        'ClassCapture_Master.zip',
        mimetype='application/zip',
        as_attachment=True
    )
