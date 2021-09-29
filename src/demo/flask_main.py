from flask import Flask
app1 = Flask(__name__)

@app1.route('/')
def hello():
    name = "Hello World"
    return name

@app1.route('/good')
def good():
    name = "Good"
    return name

## おまじない
if __name__ == "__main__":
    app1.run(debug=True)