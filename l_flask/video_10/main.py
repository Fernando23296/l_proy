from flask import Flask
from flask import render_template

app=Flask(__name__)
@app.route('/')
def index():
    name='bruno'
    return render_template('index.html',nombre=name)
if(__name__=='__main__'):
    app.run(debug=True,port=5000)