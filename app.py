from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/hello/<name>')
def hello_name(name):
    return "Hello, " + name

@app.route('/version')
def version():
    return "v2"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)
