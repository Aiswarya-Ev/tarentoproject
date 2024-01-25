# app.py
from flask import Flask, jsonify, request
from model import Database
from config import mysql_config

app = Flask(__name__)
db = Database(mysql_config)

@app.route('/api/student', methods=['GET'])
def get_student():
    db.cursor.execute('SELECT * FROM tb_student')
    student = db.cursor.fetchall()
    return jsonify({'tb_student': student})

@app.route('/api/register', methods=['POST'])
def student_reg():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    username = data.get('username')
    password = data.get('userpassword')
    type=data.get('type')

    # Insert login details into 'login' table
    db.cursor.execute('INSERT INTO tb_login (username, userpassword,type) VALUES (%s, %s, %s)', (username, password,type))
    db.db.commit()
    # Get the login id
    db.cursor.execute('SELECT LAST_INSERT_ID()')
    login_id = db.cursor.fetchone()[0]

    # Insert student details into 'students' table
    db.cursor.execute('INSERT INTO tb_student (name, email,login_id) VALUES (%s, %s, %s)', (name, email,login_id))
    db.db.commit()

    return jsonify({'message': 'Registration successful'})
@app.route('/api/login',methods=['POST'])
def login():
    data = request.get_json()
    username=data.get('username')
    userpassword=data.get('userpassword')
    db.cursor.execute('SELECT * FROM tb_login WHERE username = %s and userpassword=%s', (username,userpassword))
    results = db.cursor.fetchone()
    record_count = db.cursor.rowcount
    type_value = results[3]
    if record_count > 0:
        return jsonify({'message': f'{type_value} login successfully'})
    else:
        return jsonify({'message': 'Login failed'}), 401  # 401 for unautho
    


# ... (other API routes)

if __name__ == '__main__':
    app.run(debug=True)
