## Connecting to the database

## importing 'mysql.connector' as mysql for convenient
import mysql.connector as mysql
from datetime import datetime
import uuid

## connecting to the database using 'connect()' method
## it takes 3 required parameters 'host', 'user', 'passwd'
db = mysql.connect(
    host = "platzi-messages.cqaxfyn8oftp.us-west-2.rds.amazonaws.com",
    user = "backend",
    passwd = "backpass2020",
    database = "messages"
)

cursor = db.cursor()


query = "INSERT INTO users (name, user_name) VALUES (%s, %s)"
values = ("Hafeez", "hafeez")

now = datetime.now()
print(now)

## defining the Query
query = "INSERT INTO messages (id, type, id_thread, id_user, id_channel, message, is_public, is_pinned, is_deleted, created_at) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

## storing values in a variable
values = ("01abed46-a437-4a6e-9ddd-120bdaf09cf5", "message", "4e188d9a-b611-4dec-ad78-c10d015ec814", "a74a4abb-5fe0-43b5-94ea-462678baef11", "e2d12f75-f75b-435b-9733-caeda5668648", "Message inserted from python", 0, 0, 0, now)



## executing the query with values
#cursor.execute(query, values)

## to make final output we have to run the 'commit()' method of the database object
#db.commit()

#print(cursor.rowcount, "record inserted")

uuidOne = uuid.uuid1()
print ("Printing my First UUID of version 1")
print(uuidOne)