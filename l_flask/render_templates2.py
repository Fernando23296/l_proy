from flask import Flask
from flask import render_template

app=Flask(__name__)


@app.route('/user/')
@app.route('/user/<name>')
@app.route('/user/<name>/<int:age>')
def user(name='nombre feik',age=12):

    my_list=[1,2,3,4]
    return render_template('user1.html',nombre=name, edad=age,mi_lista=my_list)
if(__name__=='__main__'):
    app.run(debug=True,port=5000)
