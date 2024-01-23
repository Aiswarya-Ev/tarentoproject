#print("hello aisu")
import mysql.connector

# Establishing a connection to MySQL
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password@123"
)
cursor = connection.cursor()
cursor.execute("CREATE DATABASE abc")