from flask import Flask 
app = Flask(__name__)

def about():
	return "<h1>This about page </h1>"

app.add_url_rule("/about","about",about)

if __name__ == "__main__":
	app.run(debug=True)