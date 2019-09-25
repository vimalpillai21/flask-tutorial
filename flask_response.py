from flask import *

app = Flask(__name__)

@app.route("/cookie")
def cookie():
	res = make_response("<h2>Cookie is set</h2>")
	res.set_cookie('foo','bar')
	return res

if __name__ == "__main__":
	app.run(debug=True)