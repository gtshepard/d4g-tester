from flask import Flask

app = Flask(__name__)

@app.route("/")
def homepage():
    return f'home page!'

@app.route("/docs")
def docs():
    return f'docs page!'

@app.route("/about")
def about():
    return 'about page!'

if __name__ == "__main__":
    app.run(debug=True)