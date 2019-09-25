from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def message():
	return render_template('hello2.html')

if __name__ == "__main__":
	app.run(debug=True)