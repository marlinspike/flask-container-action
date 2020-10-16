from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'


@app.route('/hello/<name>')
def hello_name(name="Anonymous"):
    return f"Hello, {name}!"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)
