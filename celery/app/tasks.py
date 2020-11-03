from celery import Celery
from celery.schedules import crontab
from datetime import datetime
import mysql.connector as mysql
import time
import random
import uuid

db = mysql.connect(
    host = "platzi-messages.cqaxfyn8oftp.us-west-2.rds.amazonaws.com",
    user = "backend",
    passwd = "backpass2020",
    database = "messages"
)

celery_app = Celery('tasks', broker='redis://redis:6379/')
celery_app.conf.timezone = 'America/Bogota'

#celery_app.conf.beat_schedule = {
#    'each 2 min': {
#        'task': 'tasks.resta',
#        'schedule': crontab(minute='*/2')
#    },
#}

# id_user: a74a4abb-5fe0-43b5-94ea-462678baef11
@celery_app.task()
def insertMessage(id_thread, id_user, id_channel, message):
    cursor = db.cursor()
    now = datetime.now()
    query = "INSERT INTO messages (id, type, id_thread, id_user, id_channel, message, is_public, is_pinned, is_deleted, created_at) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    values = (str(uuid.uuid1()), "message", id_thread, id_user, id_channel, message, 0, 0, 0, now)
    cursor.execute(query, values)
    uuidOne = uuid.uuid1()
    db.commit()
    return cursor.rowcount
    #return (cursor.rowcount, "record inserted")



#    time.sleep(1)
#    uuidOne = uuid.uuid1()
#    jsonText = { 
#            "id_message": str(uuid.uuid1()), 
#            "type": "message",
#            "id_thread": id_thread,
#            "id_user": id_user,
#            "id_channel": id_channel,
#            "message": message
#            }
#    return jsonText

@celery_app.task()
def showMessage(id_thread, id_user, id_channel, message):
    time.sleep(20)
    uuidOne = uuid.uuid1()
    jsonText = { 
            "id_message": str(uuid.uuid1()), 
            "type": "message",
            "id_thread": id_thread,
            "id_user": id_user,
            "id_channel": id_channel,
            "message": message
            }
    return jsonText


