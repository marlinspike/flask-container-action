from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    #return 'Hello, World! This is v4!'
    return render_template('index.html', msg='Hello World!', title="Hello from a Docker Container!")

@app.route('/hello/<name>')
def hello_name(name):
    return render_template('index.html', msg=f"Hello, {name}!", title="Hello from a Docker Container!")
    #return "Hello, " + name


@app.route('/universe')
def universe():
    return "42"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)
