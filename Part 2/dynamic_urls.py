from flask import Flask

app=Flask(__name__)

@app.route('/')
def home():
    return "<h1>Welcome to Home Page</h1>"

@app.route('/welcome/steve')
def welcome():
    return "<h1>Hey Steve, Welcome to our page</h1>"

@app.route('/welcome/<name>') # path parameters
def welcome1(name):
    return f"<h1>Hey {name}, Welcome to our page</h1>"

if __name__ == "__main__":
    app.run(debug=True)