from flask import Flask, render_template, request, url_for
import os

PEOPLE_FOLDER = os.path.join('static', 'people_photo')

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = PEOPLE_FOLDER


@app.route('/')
@app.route('/index')
def show_index():
    full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'auto.png')
    return render_template("prueba.html", user_image=full_filename)
if(__name__=='__main__'):
    app.run(debug=True,port=5000)