from flask import Flask, render_template, request, jsonify
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
import env
import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="livecampus",
    password=env.conf["dbPassword"],
    database="classicmodels"
)
app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = env.conf["secretLocal"]
jwt = JWTManager(app)

@app.route("/")
def login():
    return render_template('login.html')
@app.route('/connexion', methods=['POST'])
def checklogin():
    username = request.json.get("username", None)
    password = request.json.get("password", None)

    if username != "admin" or password != "admin":
        return jsonify({"msg": "Mauvais identifiants"}), 401

    access_token = create_access_token(identity=username)
    print(access_token)
    return jsonify(access_token=access_token)


@app.route("/formulaire")
@jwt_required()
def hello_world():
    #return render_template('formulaire.html')
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200


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

