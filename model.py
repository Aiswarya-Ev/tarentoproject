# model.py
import mysql.connector
from config import mysql_config

class Database:
    def __init__(self, config):
        self.db = mysql.connector.connect(**config)
        self.cursor = self.db.cursor()

    def create_tables(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS tb_login (
                login_id INT AUTO_INCREMENT PRIMARY KEY,
                username VARCHAR(255) NOT NULL,
                userpassword VARCHAR(255) NOT NULL
            )
        ''')

        self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS tb_student (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    name VARCHAR(255) NOT NULL,
                    email VARCHAR(255) NOT NULL,
                    login_id INT,
                   FOREIGN KEY (login_id) REFERENCES tb_login(login_id)
           )
        ''')
        
        self.db.commit()

db = Database(mysql_config)
db.create_tables()


