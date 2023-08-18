from flask import Flask, render_template,request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')
@app.route('/usage')
def usage():
    return render_template('usage.html')
@app.route('/listof')
def listof():
    return render_template('listof.html')

