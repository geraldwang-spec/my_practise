import sqlite3
import os

print('current position', os.getcwd())
conn=sqlite3.connect('drink1.db')
cursor=conn.cursor()
conn.close()

print("sqlite ready")
