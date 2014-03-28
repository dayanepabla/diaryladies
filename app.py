from flask import Flask, render_template, request
from flask.ext.pymongo import PyMongo

app = Flask(__name__)
mongo = PyMongo(app)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/notes')
def notes():
    notes = mongo.db.notes.find()
    return render_template("notes.html", notes=notes)

@app.route('/notes/add')
def notes_add():
    return render_template("notes_add.html")

@app.route('/notes/add', methods=['POST'])
def notes_add_post():
    nota = {"tarefa":request.form["tarefa"], "data":request.form["data"]}
    mongo.db.notes.insert(nota)
    return "Tarefa adicionada com sucesso!"

@app.route('/notes/<ObjectId:id>/remover')
def tarefa_rmv(id):
    mongo.db.notes.remove(id)
    return "Removido com sucesso"

@app.route('/contacts')
def contacts():
    contacts = mongo.db.contacts.find()
    return render_template("contacts.html", contacts=contacts)

@app.route('/contacts/add')
def contacts_add():
    return render_template("contacts_add.html")

@app.route('/contacts/add', methods=['POST'])
def contacts_add_post():
    data = {"nome":request.form["nome"], "email":request.form["email"], "telefone":request.form["telefone"]}
    mongo.db.contacts.insert(data)
    return "Contato salvo com sucesso!"

@app.route('/contacts/<ObjectId:id>/remover')
def contacts_rmv(id):
    mongo.db.contacts.remove(id)
    return "Removido com sucesso"

if __name__ == '__main__':
    app.run(debug=True)
