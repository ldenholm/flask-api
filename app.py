from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "hello world"

@app.route('/dev')
def dev():
    return "dev endpoint"

if __name__ == '__main__':
    app.run(debug=True)