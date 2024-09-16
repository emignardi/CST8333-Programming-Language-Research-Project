from flask import Flask

app = Flask(__name__)

@app.route("/greeting")
def greeting():
    return "Hello"

@app.route("/greeting/<name>")
def greetingPersonal(name):
    return "Hello " + name

if __name__ == "__main__":
    app.run(debug=True)