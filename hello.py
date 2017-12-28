from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1>look morty!</h1>'

@app.route('/pets')
def my_favorite_pet():
	return 'My favorite pet is Cat!'
