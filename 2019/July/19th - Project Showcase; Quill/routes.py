from flask import Flask,redirect, render_template,request
import os
app = Flask(__name__, template_folder='static/templates')

@app.route('/', methods=["GET", "POST"])
def home():
    """Primary route handler, prints the contents out from the form submit on quill-demo.html"""
    if request.method == "POST":
        print("Heading: {}".format(request.form['Heading']))
        print("Sub-Heading: {}".format(request.form['sub-heading']))
        print("Category: {}".format(request.form['category']))
        print("Content: {}".format(request.form['content']))
    return render_template("quill-demo.html")

if __name__ == '__main__':
    app.static_folder = 'static' # Allows absolute paths to folders inside /static
    app.run(host="0.0.0.0", port=5000)
