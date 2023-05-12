from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.dojos import Dojos
from flask_app.models.ninjas import Ninjas

@app.route('/')
def index():
    dojos = Dojos.read_all()
    return render_template("dojos.html",dojos=dojos)

@app.route('/new_dojo', methods = ['POST'])
def new():
    data = {
        'name' : request.form['name'],
    }
    Dojos.new_dojo(data)
    return redirect('/')

@app.route('/dojo_details/<int:id>')
def show_dojo(id):
    data = {
        'id' : id
    }
    return render_template("details.html",dojo=Dojos.dojos_with_ninjas(data))

