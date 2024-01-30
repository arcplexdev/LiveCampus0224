from flask import Flask, render_template, request, jsonify
import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="livecampus",
    password="demoPwd",
    database="classicmodels"
)
app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('home.html')

@app.route("/bonjour/<username>")
def hello_again(username):
    return render_template('home.html',name=username)

@app.route("/formulaire")
def displayForm():
    return render_template('formulaire.html')

@app.route("/formulaire2")
def displayFormTwo():
    return render_template('form2.html')

@app.route("/traitement", methods=['POST'])
def traitement_form():
    client = request.form['client']
    # Requete 1
    sql = "SELECT * from payments where customerNumber = " + str(client) + ";"
    mycursor = mydb.cursor()
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    return render_template('resultat.html',name=client,data=myresult)

@app.route("/traitementjson", methods=['POST'])
def get_data():
    client = request.form['client']
    # Requete 1
    sql = "SELECT * from customers where customerNumber = " + str(client) + ";"
    mycursor = mydb.cursor()
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    data = {
        'client': client,
        'data': myresult[0]
    }
    return jsonify(data=data)


if __name__ == "__main__":
    app.run(debug=True)

