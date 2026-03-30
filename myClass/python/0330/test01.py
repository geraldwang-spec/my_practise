import sqlite3

conn = sqlite3.connect('test.db')
cursor = conn.cursor()

cursor.execute("""
create table if not exists students(
id integer primary key autoincrement,
name text,
age integer
)
               """)


cursor.execute(
    "insert into students(name,age) values (?,?)", ("tom", 18)
)
cursor.execute(
    "insert into students(name,age) values (?,?)", ("mary", 20)
)
conn.commit()
conn.close()


# CREATE TABLE "cat1" (
# 	"id"	INTEGER,
# 	"name"	TEXT,
# 	"age"	INTEGER,
# 	PRIMARY KEY("id" AUTOINCREMENT),
# 	FOREIGN KEY("id") REFERENCES ""
# );
