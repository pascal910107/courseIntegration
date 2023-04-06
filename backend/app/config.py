from pymongo import MongoClient
import datetime

client = MongoClient('mongodb://courseintegration-mongodb-1:27017/')
db = client['courseintegration']

now = datetime.datetime.now()
if now.month >= 8:
    year = now.year - 1911
else:
    year = now.year - 1912

if now.month >= 2 and now.month <= 7:
    semester = 2
else:
    semester = 1