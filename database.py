import mysql.connector

conn = mysql.connector.connect(
    host = 'localhost',
    user='root',
    password = '',
    database ='cadastro'   
)
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        ID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,    
        Username VARCHAR(100) UNIQUE NOT NULL,
        Email VARCHAR(100) NOT NULL,
        Password VARCHAR(100) NOT NULL
        )    
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS logins (                    
        ID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,    
        Username VARCHAR(100) UNIQUE NOT NULL,
        Email VARCHAR(100) NOT NULL,
        Password VARCHAR(100) NOT NULL,
        Local_user VARCHAR (250)       
        )   
""")

print("Conexão de dados feita com sucessos!")
