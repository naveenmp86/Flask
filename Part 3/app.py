from flask import Flask,render_template,url_for
from employees import employees_data

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html",title="Naveen M P")

@app.route("/about")
def about():
    return render_template("about.html",title="about")

@app.route("/welcome/<name>")
def welcome(name):
    return f"<h1>Hii {name.title()}, Welcome to Home Page</h1>"

@app.route("/evaluate/<int:num>")
def evaluate(num):
    return render_template("evaluate.html",title="Evaluate",number=num)

@app.route("/employees")
def employees():
    return render_template("employees.html",title="Employees",employees=employees_data)

@app.route("/employees/managers")
def managers():
    return render_template("managers.html",title="Managers",employees=employees_data)


@app.route("/addition/<int:num1>/<int:num2>")
def addition(num1,num2):
    return f"<h1>Result is {num1 * num2}</h1>"

if __name__ == "__main__":
    app.run(debug=True)