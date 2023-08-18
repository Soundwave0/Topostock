from flask import Flask, render_template,request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('C:\\Users\\konch\\Downloads\\__pycache__\\templates\\home.html')
