from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def hello():
    #return 'Hello, World! This is v4!'
    return render_template('index.html', msg='Hello World!', title="Hello from a Docker Container!")

@app.route('/hello/<name>')
def hello_you(name):
    #return 'Hello, World! This is v4!'
    return render_template('index.html', msg=f"Hello {name}!", title="Hello from a Docker Container!")


@app.route('/universe')
def universe():
    return "42"

@app.route('/add/<int:num1>/<int:num2>')
def add(num1, num2):
    sum = num1 + num2
    message = f"{num1} + {num2} = {sum}"
    return render_template('index.html', msg=message, title="Hello from a Docker Container!")


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)
