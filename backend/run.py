from app.app import app
from pymongo import MongoClient

if __name__ == '__main__':
    client = MongoClient("mongodb://classrushsystem-mongodb-1:27017/")
    db = client["classrushsystem"]
    if "users" not in db.list_collection_names():
        db.create_collection("users")
    app.run(host='0.0.0.0')