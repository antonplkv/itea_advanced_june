import sqlite3

conn = sqlite3.connect('lesson_db.db')

cursor = conn.cursor()

user_number = 35000.0
cursor.execute('UPDATE cars SET price = price + 2000 WHERE id = 7')

conn.commit()

conn.close()