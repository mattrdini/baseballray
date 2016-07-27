# imports
from flask import Flask


# App itself (object + magic object) double underscore 'name' looks to filename
app = Flask(__name__)


# @ = 'decorator'

@app.route('/')
def hello():
    return "Hello World"


@app.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)












if __name__ == '__main__':
    app.run()
