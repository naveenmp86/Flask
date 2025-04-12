from flask import Flask,redirect,url_for

app=Flask(__name__)

@app.route('/')
def home():
    return "<h1>Welcome to Home Page</h1>"

@app.route('/pass/<sname>/<marks>')
def passed(sname,marks):
    return f"<h1>Congratulations {sname.title()}, You Cleared the Exams with {marks} marks!</h1>"

@app.route('/fail/<sname>/<marks>')
def failed(sname,marks):
    return f"<h1>Sorry {sname.title()}, You Failed the Exam with {marks} marks</h1>"

@app.route('/score/<name>/<int:num>')
def score(name,num):
    if num < 30:
        return redirect(url_for("failed",sname=name, marks=num))
    else:
        return redirect(url_for("passed",sname=name, marks=num))

if __name__ == "__main__":
    app.run(debug=True)