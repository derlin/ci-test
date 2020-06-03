import mysql.connector
from mysql.connector import Error

try:
    conn = mysql.connector.connect(
        host='127.0.0.1',
        database='bbdata2',
        user='bbdata-admin',
        password='bbdata')

    if conn.is_connected():
       cursor = conn.cursor()
       cursor.execute("select * from objects;")
       records = list(cursor.fetchall())
       print(f'Got {len(records)} objects.')
except Error as e :
    print ("ERROR", e)
    exit(1)

finally:
    #closing database connection.
    if(conn.is_connected()):
       cursor.close()
       conn.close()