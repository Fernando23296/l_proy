#FICHERO PARA CONECTAR CON UNA VISTA QUE RECOGE 'FRAGMENTOS', FLYWEIGHT
from flask import Flask
from flask import render_template

app= Flask(__name__)
@app.route('/')
def index():
    return 'khe'


@app.route('/client/')
@app.route('/client/<name>')
def client(name='default'):
    return render_template('index_fragmentado.html',nombre=name)
@app.route('/lista')
def lista():
    milista=['bruno','fernando','silva','plata']
    return render_template('index_fragmentado2.html',milista=milista)
if(__name__=='__main__'):
    app.run(debug=True,port=5000)
