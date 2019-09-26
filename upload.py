from flask import *

app = Flask(__name__)

@app.route("/")
def upload():
    return render_template("file_upload_form.html")

@app.route("/success",methods=['POST'])
def success():
    if request.method == "POST":
        file = request.files['file']
        print(file)
        file.save(file.filename)
        return render_template("file_success.html",name=file.filename)

if __name__ == "__main__":
    app.run(debug=True)