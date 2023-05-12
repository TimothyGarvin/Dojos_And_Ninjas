from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.ninjas import Ninjas
from flask_app.models.dojos import Dojos

@app.route('/ninjas/new')
def create_new():
    dojos=Dojos.read_all()
    return render_template('new_ninja.html', dojos=dojos)

@app.route('/new_ninja', methods=['POST'])
def create():
    data = {
        'first_name' : request.form['first_name'],
        'last_name' : request.form['last_name'],
        'age' : request.form['age'],
        'dojo_id' : request.form['dojo_id']
    }
    Ninjas.create(data)
    return redirect('/')

