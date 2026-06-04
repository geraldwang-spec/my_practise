import sqlite3
from pathlib import Path

class SqliteProcess:
    def __init__(self, db = "login.db") -> None:
        self.db = db
        self.connected = self.__init_sql_database(db)

    def __init_sql_database(self, db):
        b = True
        if Path("login.db").is_file():
            return b
        con = sqlite3.connect(db)
        try:
            with con as con:
                cur = con.cursor()
                cur.execute("""
               CREATE TABLE "login" (
                        	"id"	INTEGER,
                        	"username"	TEXT NOT NULL UNIQUE,
                        	"passwd"	TEXT NOT NULL,
                        	"email"	TEXT NOT NULL UNIQUE,
                        	"name"	TEXT NOT NULL UNIQUE,
                        	"mail_ready"	INTEGER NOT NULL,
                        	"mail_number"	INTEGER NOT NULL,
                        	"account_created"	TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
                        	"mail_check_time"	TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
                        	PRIMARY KEY("id" AUTOINCREMENT)
                        ); 
                """)
                print("create db")
        except sqlite3.Error as e:
            print(f"login.db init fail: {e}")
            b = False
        finally:
            print("db init finish")
            con.close()
        
        return b

    def get_login_data(self):
        rows = []
        con = sqlite3.connect(self.db)
        try:
            with con:
                cur = con.cursor()
                _ = cur.execute("""
                                select 
                                username, 
                                passwd, 
                                email, 
                                name, 
                                mail_ready,
                                mail_number,
                                account_created,
                                mail_check_time,
                                from login
                                """)
                rows = cur.fetchall()
        except sqlite3.Error as e:
            print(f"get db data fail: {e}")
            rows = []
        finally:
            con.close()

        return rows
                




    

