import os

from flask import Flask, request, render_template, send_from_directory
import cv2

__author__ = 'ibininja'

app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))


@app.route("/")
def index():
    return render_template("upload.html")


@app.route("/upload", methods=["POST"])
def upload():
    
    target = os.path.join(APP_ROOT,'static')
    print(target)

    if not os.path.isdir(target):
        os.mkdir(target)

    for file in request.files.getlist("file"):
        print(file)
        filename=file.filename
        destination = "/".join([target, filename])
        print("Save it to:", destination)
        file.save(destination)


        ruta='static/'+filename
        img = cv2.imread(ruta, cv2.IMREAD_COLOR)
        width = img.shape[1]
        print(width)
    print(filename)
    #filenamepro='/images/'+filename
    #img = cv2.imread(filenamepro, cv2.IMREAD_COLOR)
    #height = img.shape[0]
    #print(height)
    # return send_from_directory("images", filename, as_attachment=True)
    return render_template("complete.html",image_name=filename)



if __name__ == "__main__":
    app.run(port=4555, debug=True)
