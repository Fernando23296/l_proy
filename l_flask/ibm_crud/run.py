from flask import Flask, redirect, url_for, request, render_template, make_response, session, abort, flash
from werkzeug import secure_filename
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = 'XYZ'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:password@localhost/mysql'

db = SQLAlchemy(app)

class AddressBook(db.Model):
    id = db.Column('id', db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    city = db.Column(db.String(50))
    addr = db.Column(db.String(200))
    pin = db.Column(db.String(10))

    def __init__(self, name, city, addr, pin):
        self.name = name
        self.city = city
        self.addr = addr
        self.pin = pin

@app.route('/address')
def address():
    db.create_all()
    return render_template('address.html')


@app.route('/show_all')
def show_all():
    return render_template('show_all.html', addresses = AddressBook.query.all())


@app.route('/show_update', methods=['POST', 'GET'])
def show_update():
    id = request.args.get('id')
    address = AddressBook.query.filter_by(id=id).first()
    return render_template('update_addr.html', address=address)


@app.route('/show_new')
def show_new():
    return render_template('newaddress.html')


@app.route('/new_addr', methods=['POST', 'GET'])
def new_addr():
    if request.method == 'POST':
        address = AddressBook(request.form['nm'], request.form['city'],request.form['add'],request.form['pin'])
        db.session.add(address)
        db.session.commit()
    return render_template('show_all.html', addresses = AddressBook.query.all())

@app.route('/delete_addr')
def delete_addr():
    id = request.args.get('id')
    address = AddressBook.query.filter_by(id=id).first()
    db.session.delete(address)
    db.session.commit()
    return render_template('show_all.html', addresses = AddressBook.query.all())


@app.route('/update_addr', methods=['POST', 'GET'])
def update_addr():
    if request.method == 'POST':
        print ("Inside POST")
        try:
            id = request.form['id']
            address = AddressBook.query.filter_by(id=id).first()
            address.name = request.form['nm']
            address.addr = request.form['add']
            address.city = request.form['city']
            address.pin = request.form['pin']
            db.session.commit()
        except:
            msg = "error during update operation"
            print (msg)
    return render_template('show_all.html', addresses = AddressBook.query.all())