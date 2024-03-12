from flask import Flask, render_template, request
import requests


app = Flask(__name__)
template_folder = 'template'


@app.route('/')
def index():
    return render_template('home.html')


@app.route('/result')
def index():
    return render_template('result.html')


if __name__ == '__main__':
    app.run(debug=True)
