from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    #return 'Hello, World! This is v4!'
    return render_template('index.html', msg='Hello World!', title="Hello from a Docker Container!")


@app.route('/universe')
def universe():
    return "42"

@app.route('/add/<int:num1>/<int:num2>')
def add(num1, num2):
    sum = num1 + num2
    return f"{sum}"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)
