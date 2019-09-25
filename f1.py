from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
	return 'Hello, World'


@app.route('/homes')
def home_page():
		return 'Welcome to the home page!'

@app.route('/home/<name>')
def home_page_2(name):
	return "Hello, "+name

if __name__ == "__main__":
	app.run(debug=True)
