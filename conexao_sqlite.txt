import sqlite3

conn =sqlite3.connect("cadastro.db")

cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
     ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
               Username UNIQUE  NOT NULL,
               Email VARCHAR NOT NULL,
               Password VARCHAR NOT NULL
               )
""")
cursor.execute("""
    CREATE TABLE IF NOT EXISTS logins (
     ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
               Username UNIQUE NOT NULL,
               Email VARCHAR NOT NULL,
               Password VARCHAR NOT NULL
               )
""")

print("Conexão de dados feita com sucessos!")