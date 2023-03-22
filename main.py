from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>hello, world</p>"


@app.route("/greet/user/<username>/<int:number>")
def greet(username, number):
    return f"welcome! {username}. you are user {number}"


if __name__ == "__main__":
    app.run(debug=True)
