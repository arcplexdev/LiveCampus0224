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
    return render_template('formulaire.html')

@app.route("/traitement", methods=['POST'])
def traitement_form():
    client = request.form['client']
    sql = "select customerName from customers where customerNumber = "  + str(client) + ";"
    mycursor = mydb.cursor()
    mycursor.execute(sql)
    myclient = mycursor.fetchall()

    if len(myclient) == 1:
        sql = "SELECT * from payments where customerNumber = " + str(client) + ";"
        mycursor = mydb.cursor()
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        if len(myresult) == 0:
            return "Pas de paiements pour ce client <a href='/'>Retour</a>"
        else:
            return render_template('resultat.html',name=client,data=myresult,client=myclient)
    else:
        return "Ce numero de dossier n'existe pas <a href='/'>Retour</a>"


if __name__ == "__main__":
    app.run(debug=True)

