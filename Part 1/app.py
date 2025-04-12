from flask import Flask

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return "<h1>Welcome to the Home Page!</h1>"

@app.route("/about")
def about():
    return "<h1>Welcome to the About Page</h1>"

@app.route("/welcome/<name>")
def welcome(name):
    return f"<h1>Hii {name.title()}, Welcome to Home Page</h1>"


@app.route("/addition/<int:num1>/<int:num2>")
def addition(num1,num2):
    return f"<h1>Result is {num1 * num2}</h1>"

if __name__ == "__main__":
    app.run(debug=True)