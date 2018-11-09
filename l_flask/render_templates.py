from flask import Flask
from flask import render_template

app=Flask(__name__)
'''
por si la carpeta de templates tiene otro nombre:
app=Flask(__name__,template_folfer="prueba_template")s
'''

@app.route('/')
def index():
    return render_template('index1.html')

if (__name__=='__main__'):
    app.run(debug=True,port=5000)
