from flask import Flask, request
from flask_cors import CORS
from pymongo import MongoClient
import requests
from bs4 import BeautifulSoup
import json
import os
from dotenv import load_dotenv
from bson import json_util


app = Flask(__name__)
CORS(app)

load_dotenv()
year = os.getenv('YEAR')
semester = os.getenv('SEMESTER')

@app.route('/api/login', methods=['POST'])
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
        data = json.loads(response.text)
        inner_data = json.loads(data['d'])
        
        if inner_data['user']['isAnonymus'] == False and inner_data['user']['detail'] != None:
            
            try:
                client = MongoClient('mongodb://classrushsystem-mongodb-1:27017/')
                db = client['classrushsystem']
                query = {'user.detail.name.cht': inner_data['user']['detail']['name']['cht']}
                result = db.user.find_one(query)
                if result:
                    db.user.replace_one(query, inner_data)
                else:
                    db.user.insert_one(inner_data)
            except Exception as e:
                return str(e)
            return inner_data
        return 'false'
    else:
        return 'false'


# @app.route('/api/logout', methods=['POST'])

@app.route('/api/users', methods=['GET'])
def getUser():
    client = MongoClient('mongodb://classrushsystem-mongodb-1:27017/')
    db = client['classrushsystem']
    cursor = db.user.find()
    python_list = list(json.loads(json_util.dumps(doc, default=json_util.default)) for doc in cursor)
    return python_list


# @app.route('/api/users/<id>', methods=['GET'])


@app.route('/api/courses', methods=['GET'])
def getCourses():
    rs = requests.session()
    response = rs.get('https://myfcu.fcu.edu.tw/main/InfoMyFcuLogin.aspx')
    soup = BeautifulSoup(response.text, 'html.parser')
    headers = {
        'Accept': '*/*',
        'Accept-Language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Origin': 'https://myfcu.fcu.edu.tw',
        'Referer': 'https://myfcu.fcu.edu.tw/main/InfoMyFcuLogin.aspx',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
        'X-MicrosoftAjax': 'Delta=true',
        'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    data = {
        'ScriptManager1': 'UpdatePanel1|OKButton',
        '__LASTFOCUS': '',
        '__EVENTTARGET': '',
        '__EVENTARGUMENT': '',
        '__VIEWSTATE': soup.select_one('#__VIEWSTATE')['value'],
        '__VIEWSTATEGENERATOR': soup.select_one('#__VIEWSTATEGENERATOR')['value'],
        '__SCROLLPOSITIONX': '',
        '__SCROLLPOSITIONY': '',
        '__EVENTVALIDATION': soup.select_one('#__EVENTVALIDATION')['value'],
        'txtUserName': 'D0957293',
        'txtPassword': 'brian45455975',
        'csrf_token': soup.select_one('#csrf_token')['value'],
        '__ASYNCPOST': 'true',
        'OKButton': 'login',
    }

    response = rs.post('https://myfcu.fcu.edu.tw/main/InfoMyFcuLogin.aspx', headers=headers, data=data)

    response = requests.post(
        'https://myfcu.fcu.edu.tw/main/S3202/S3202_timetable_new.aspx/GetCurriculum',
        cookies = rs.cookies,
        json = {
            'year': year,
            'smester': semester,
        },
    )
    data = json.loads(response.text)
    return data['d']



@app.route('/api/', methods=['GET'])
def hello():
    client = MongoClient('mongodb://classrushsystem-mongodb-1:27017/')
    # db_list = client.list_database_names()
    db = client['classrushsystem']
    # db.create_collection('users')
    # collections = db.list_collection_names()
    # return collections

    load_dotenv()
    year = os.getenv('YEAR')
    semester = os.getenv('SEMESTER')
    response = requests.post(
        'https://coursesearch04.fcu.edu.tw/Service/Auth.asmx/login',
        json = {
            'id': 'D0957293',
            'password': 'brian45455975',
            'baseOptions': {
                'lang': 'cht',
                'year': year,
                'sms': semester,
            },
        },
    )
    data = json.loads(response.text)
    inner_data = json.loads(data['d'])

    cursor = db.user.find()
    python_list = list(json.loads(json_util.dumps(doc, default=json_util.default)) for doc in cursor)
    return python_list
    # return inner_data
