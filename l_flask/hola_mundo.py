from flask import Flask
app=Flask(__name__) # nuevo objeto
@app.route('/') #wrap o decorador
def index():
    return "hola"
app.run()