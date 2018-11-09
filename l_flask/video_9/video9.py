from flask import Flask
from flask import render_template
app=Flask(__name__)


@app.route('/video9/')
@app.route('/video9/<name>')
def video9(name='default'):
    return render_template('index.html',nombre=name)
if(__name__=='__main__'):
    app.run(debug=True,port=5000)
