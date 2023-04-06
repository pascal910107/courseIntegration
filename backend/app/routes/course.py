from flask import Blueprint, request
import requests
from bs4 import BeautifulSoup
import json

from app.config import db, year, semester
from app.routes.user import check_user_exists, get_user_account_secret

course_bp = Blueprint('course', __name__, url_prefix='/api/courses')


def update_data_to_database(id, response_data):
    db.courses.update_one(
        {"id": id},
        {"$set": {"courses": response_data['d']}},
        upsert=True
    )

def query_data_from_database(id):
    return db.courses.find_one({"id": id})['courses']


def update_data(id, password):
    rs = requests.session()
    response = rs.get('https://myfcu.fcu.edu.tw/main/InfoMyFcuLogin.aspx')
    soup = BeautifulSoup(response.text, 'html.parser')
    headers = {
        'Accept': '*/*',  # 接受任何內容的回應
        'Accept-Language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7',  # 接受語言的優先順序
        'Cache-Control': 'no-cache',  # 告訴伺服器不要快取回應
        'Connection': 'keep-alive',  # 使用持續連線
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',  # 請求的內容類型
        'Origin': 'https://myfcu.fcu.edu.tw',  # 請求的來源
        'Referer': 'https://myfcu.fcu.edu.tw/main/InfoMyFcuLogin.aspx',  # 表示請求的頁面
        'Sec-Fetch-Dest': 'empty',  # 防止跨站請求偽造(CSRF)攻擊
        'Sec-Fetch-Mode': 'cors',  # 跨來源請求(CORS)模式
        'Sec-Fetch-Site': 'same-origin',  # 限制僅允許從相同的網域發送請求
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',  # 表示用戶端的軟體應用程式
        'X-MicrosoftAjax': 'Delta=true',  # 標記一個請求是由 Microsoft AJAX 生成的
        'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',  # 請求的用戶端代理的資訊
        'sec-ch-ua-mobile': '?0',  # 指示使用的裝置是否是行動裝置
        'sec-ch-ua-platform': '"Windows"',  # 指定使用的裝置平台
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
        'txtUserName': id,
        'txtPassword': password,
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
    response_data = json.loads(response.text)
    if response_data['d'] == '75FF57F7-7AC0-43c8-9454-C92B4A2723BB':
        return 'false'
    try:
        update_data_to_database(id, response_data)
        return response_data['d']
    except Exception as e:
        return str(e)





@course_bp.route('/', methods=['GET'])
def get_courses():
    user_id = request.args.get('id', default=None, type=str)

    if check_user_exists(user_id):
        format = request.args.get('format', default='table', type=str)
        result = query_data_from_database(user_id)
        if format == 'list':
            return result['list']
        else:
            return result['table']
    else:
        return 'id not found'


@course_bp.route('/refresh/', methods=['GET'])
def refresh_courses():
    user_id = request.args.get('id', default=None, type=str)
    format = request.args.get('format', default='table', type=str)

    data = get_user_account_secret(user_id)
    result = update_data(data['id'], data['password'])
    if result == 'false':
        return 'id or password error'
    else:
        if format == 'list':
            return result['list']
        else:
            return result['table']


