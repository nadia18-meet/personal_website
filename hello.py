from flask import Flask
app = Flask(__name__)

@app.route('/home')
def home():
	return 'home.html'

@app.route('/categories')
def categories():
	return 'categories.html'

@app.route('/add')
def add():
	return 'add.html'



