from flask import Flask
from flask import request
app = Flask(__name__)


@app.route('/')
def index():
    return "hola esto es ejemplo 2"


@app.route('/params/')
#<name> para evitar poner el ?
@app.route('/params/<name>')
@app.route('/params/<name>/<int:num>')


def params(name='nombre default',num='numero defualt'):
    return 'Lo que escribiste es: {} {}'.format(name,num)


if (__name__ == '__main__'):
    app.run(debug=True, port=5000)
