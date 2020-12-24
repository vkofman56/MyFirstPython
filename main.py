from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return '<h3>This is Home Page</h3>'