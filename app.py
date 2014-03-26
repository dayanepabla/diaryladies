from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/diary')
def diary():
    return render_template("diary.html")

@app.route('/contacts')
def contacts():
    return render_template("contacts.html")

@app.route('/contacts/add')
def contacts_add():
    return render_template("contacts_add.html")

@app.route('/contacts/add', methods=['POST'])
def contacts_add_post():
      return "Contato salvo com sucesso!"

if __name__ == '__main__':
    app.run(debug=True)
