import mysql.connector 
from flask import Flask, jsonify, make_response, request

app = Flask(__name__)

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="Byme"   
)

@app.route('/register', methods=['POST'])
def register():
    new_user=request.get_json()
    my_cursor=mydb.cursor()

    query = f"INSERT INTO livros (email, pass) VALUES ('{new_user['email']}', {new_user['password']})"
    my_cursor.execute(query)
    mydb.commit()

    return make_response(
        jsonify(
            msg = 'User created successfully',
            succes = True,
            data = new_user
        ),
        201
    )


app.run(port=5000,host='localhost',debug=True)
