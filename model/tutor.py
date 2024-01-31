import mysql.connector #connect sql
from flask import Flask, jsonify, request #convert Python dictionaries to JSON format 
from config import mysql_config

app = Flask(__name__)
db = mysql.connector.connect(**mysql_config)
cursor = db.cursor()

def tut():
    try:
        db.cursor.execute('SELECT * FROM tb_tutor')
        tutor = db.cursor.fetchall()
        return jsonify({'tb_tutor': tutor})
    except Exception as e:
        return jsonify({'error': str(e)})

















@app.route('/api/tutor', methods=['GET'])
def get_tutorr():
    return tut()