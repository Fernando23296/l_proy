from flask import Flask
app = Flask(__name__)  # nuevo objeto


@app.route('/')  # wrap o decorador
def index():
    return "hola mundo que onda"

@app.route('/saludo')
def saludo():
    return "esto es un saludo"


if (__name__ == '__main__'):  # deberia dar auqnue tenga los parentesis
    app.run(debug=True, port=5000)
