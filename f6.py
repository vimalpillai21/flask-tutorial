from flask import *

app = Flask(__name__)

@app.route('/login/',methods=['GET'])
def login():
	print(request.args)
	uname = request.args.get('uname')
	password = request.args.get('pass')
	if uname == "vimal" and password == "google":
		return "Welcome %s"%uname

if __name__ == "__main__":
	app.run(debug=True)