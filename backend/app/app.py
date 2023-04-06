from flask import Flask, request
from flask_cors import CORS, cross_origin
import requests
from bs4 import BeautifulSoup
import json
from bson import json_util
from app.config import db, year, semester

from app.routes.course import course_bp, update_data
from app.routes.user import user_bp



app = Flask(__name__)
CORS(app)


# import os
# from dotenv import load_dotenv
# load_dotenv()
# year = os.getenv('YEAR')
# semester = os.getenv('SEMESTER')



# course blueprint
app.register_blueprint(course_bp)
# user blueprint
app.register_blueprint(user_bp)


@app.route('/api/login', methods=['POST'])
@cross_origin()
def login():
    if request.is_json:
        data = request.get_json()
        response = requests.post(
            'https://coursesearch04.fcu.edu.tw/Service/Auth.asmx/login',
            json = {
                'id': data['id'],
                'password': data['password'],
                'baseOptions': {
                    'lang': 'cht',
                    'year': year,
                    'sms': semester,
                },
            },
        )
        response_data = json.loads(response.text)
        inner_data = json.loads(response_data['d'])
        
        if not inner_data['user']['isAnonymus'] and inner_data['user']['detail']:
            
            try:
                query = {'user.detail.name.cht': inner_data['user']['detail']['name']['cht']}
                result = db.users.find_one(query)

                if result:
                    db.users.replace_one(query, inner_data)
                else:
                    db.users.insert_one(inner_data)
                    # db.accounts.insert_one(account)
                db.accounts.update_one(
                    {"id": data['id']},
                    {"$set": {"password": data['password']}},
                    upsert=True
                )
                update_data(data['id'], data['password'])
                return json_util.dumps(inner_data)
            except Exception as e:
                return str(e)
    return 'false'




@app.route('/api/', methods=['GET'])
def hello():
    # db_list = client.list_database_names()
    
    #回傳所有collection名稱
    # collections = db.list_collection_names()
    # return collections

    # result = db['accounts'].find_one({'id': 'd'})
    # return str(result == None)

    #回傳所有accounts內的資料
    # data = list(db['accounts'].find())
    # for item in data:
    #     item['_id'] = str(item['_id'])
    # return data

    #回傳所有courses內的資料
    data = list(db['courses'].find())
    for item in data:
        item['_id'] = str(item['_id'])
    return data


    #回傳所有users內的資料，並把_id從查詢結果中刪除
    data = list(db['users'].find({}, {'_id': 0}))
    return data

    # return str(year) + str(semester)