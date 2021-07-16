import sqlite3


db = sqlite3.connect(database="srms.db")
cur = db.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS users(name VARCHAR NOT NULL,contact BIGINT NOT NULL,"
            "email VARCHAR PRIMARY KEY NOT NULL,roll CHAR,password VARCHAR NOT NULL,question VARCHAR NOT NULL,"
            "answer VARCHAR NOT NULL,faculty VARCHAR NOT NULL,semester VARCHAR NOT NULL,year VARCHAR NOT NULL,"
            "gender SMALLINT NOT NULL,profession SMALLINT NOT NULL,permission tinyint,tu_registered_id int)")

cur.execute("CREATE TABLE IF NOT EXISTS result(rid INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,email VARCHAR NOT NULL,"
            "marks TEXT NOT NULL,FOREIGN KEY(email) REFERENCES users(email))")
