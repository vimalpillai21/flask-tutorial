from flask import *

app = Flask(__name__)

@app.route('/login/',methods=['POST'])
def login():
	uname = request.form.get('uname')
	password = request.form.get('pass')
	if uname == "Vimal" and password == "google":
		return "Welcome %s"%uname
	else:
		return "Sorry! you have entered the wrong credentials"

if __name__ == "__main__":
	app.run(debug=True)