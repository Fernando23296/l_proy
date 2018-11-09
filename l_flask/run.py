from flask import Flask
app = Flask(__name__)  # nuevo objeto


@app.route('/')  # wrap o decorador
def index():
    return "hola mundo que onda"

if (__name__ == '__main__'):
    app.run(debug=True, port=5000)
