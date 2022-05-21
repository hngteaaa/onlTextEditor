from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__, static_folder= 'static', template_folder='template')

User_acc = ["", ""]

@app.route('/', methods=['GET', 'POST'])
def homepage():
    return render_template("homepage.html")

if __name__ == "__main__":
    app.run(port=5000, debug=True)