# model/program
import mysql.connector
import bcrypt
from config import mysql_config
from flask import Flask, jsonify, request
db = mysql.connector.connect(**mysql_config)
cursor = db.cursor()


def selectAllStudent():
    cursor.execute('SELECT * FROM tb_student')
    student =cursor.fetchall()
    return jsonify({'tb_student': student})