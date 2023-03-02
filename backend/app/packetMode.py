import re
from cv2 import imshow, threshold
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import base64
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import pytesseract
from PIL import Image
import matplotlib.pyplot as plt
import cv2
import numpy as np
import threading
from requests.structures import CaseInsensitiveDict
import os
import threading
from dotenv import load_dotenv


def captchaConversion1():

    img = Image.open('./images/captcha_login.jpg').convert('L')
    table=[]
    for i in range(256):
        if i<127:
            table.append(0)
        else:
            table.append(1)
    img = img.point(table,'1')
    img.save('./images/out.jpg')
    # img.show()


    img = Image.open('./images/out.jpg')
    pixel_matrix = img.load()
    for column in range(1, 21):
        for row in range(1, 49):
            if pixel_matrix[row, column] == 0 and pixel_matrix[row, column - 1] == 255 and pixel_matrix[row, column + 1] == 255 :
                pixel_matrix[row, column] = 255
            if pixel_matrix[row, column] == 0 and pixel_matrix[row - 1, column] == 255 and pixel_matrix[row + 1, column] == 255:
                pixel_matrix[row, column] = 255
    # img.show()


    text = pytesseract.image_to_string(img)
    return "".join(list(filter(str.isdigit, text)))


def captchaConversion2():

    dst = cv2.imread('./images/captcha_login.jpg')
    ret,thresh = cv2.threshold(dst,127,255,cv2.THRESH_BINARY_INV)
    cv2.imwrite('./images/out.jpg', thresh)
    plt.imshow(thresh)
    # plt.show()

    img = Image.open('./images/out.jpg').convert('L')
    table=[]
    for i in range(256):
        if i>127:
            table.append(1)
        else:
            table.append(0)
    img = img.point(table,'1')
    img.save('./images/out.jpg')
    # img.show()


    image = cv2.imread('./images/out.jpg')
    dst = cv2.fastNlMeansDenoisingColored(image, None, 67, 67, 7, 21)
    cv2.imwrite('./images/out.jpg', dst)
    plt.imshow(dst)
    # plt.show()
   

    text = pytesseract.image_to_string(dst)
    text = text.replace('S','5').replace('$','5').replace('e','0')
    return "".join(list(filter(str.isdigit, text)))


def login(studentId, password, rs):

    headers = {
        # 'Accept-Encoding': 'gzip, deflate, sdch',
        'Accept-Language': 'en-US,en;q=0.8',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Referer': 'http://www.wikipedia.org/',
        'Connection': 'keep-alive',
    }

    response = rs.get('https://course.fcu.edu.tw/validateCode.aspx', headers=headers)

    if not os.path.exists("images"):
        os.mkdir("images")

    with open("./images/captcha_login.jpg", "wb") as image:
        image.write(response.content)
    text = captchaConversion1()
    if len(text) != 4:
        text = captchaConversion2()
        if len(text) != 4:
            return False

    data = {
        '__EVENTTARGET': 'ctl00$Login1$LoginButton',
        '__EVENTARGUMENT': '',
        '__LASTFOCUS': '',
        '__VIEWSTATE': 'Pa+vadr6mRRqfhqmRZiD9mpqR8Ngp9KcMBk5R88HN6ph0PqJV7W6mxBN1CitvSEK021BDKxYnqsdKL0Nqd1I5ZcACRh3avbSqoKkOtagQArCbQiUTu3lLg81stvRWjcz5Q9CPlveEgOkqRtZEiDOCO77qvYtTPZMysqtu4VNfeEGnGYPe7DVY8bXSoLWyHxiWhOYCqmg+565TozAaMIYISnqOARanxaCI2TWiDZY+j29J6oiv6fTMj+JA8Xcf73bbnc01LTirFbTr1ulpG0nqHJaorEi1UclRLooriABtRMWSfvvATr45Jl8ya9ak7PtbTMhx44OWZm1xNdAxLcEEwvbo/A4irPFFWuSoIuLHnZ3H+v9q/OCdOddg9rENktB6wqGLuEUZ8d5FJ3QtW1mwS4lNGJutISOOgiajIR2MWeVtVY0Rot1hd7QLlDY1FL4tQVWCwVwSQOZIfpslWIaGr/nmXx98ZdwlD7jDREpoMkGazOd/P4nO7c7IlDy1bihHjB3BPO0aDFzJa0Xiq4kS9ugivc=',
        '__VIEWSTATEGENERATOR': 'C2EE9ABB',
        '__VIEWSTATEENCRYPTED': '',
        '__EVENTVALIDATION': 'q0xl6sf49NENoAS4sowp79LBKuceZJcdJaoZ7dziVoi/KydbLvT9jeVEoXvw0+DyiD0r7OIhUx/n9FLYIrTd46d7PJlOjRN7GuzpTrl/Sl/q1h8pq7XqRKzAc9KDUzcJqmHuw1LzSkKP3xYV/6vRcoH2ctc=',
        'ctl00$Login1$RadioButtonList1': 'zh-tw',
        'ctl00$Login1$UserName': studentId,
        'ctl00$Login1$Password': password,
        'ctl00$Login1$vcode': text,
        'ctl00$temp': '',
    }

    response = rs.post('https://course.fcu.edu.tw/Login.aspx', data=data)
    if response.url == 'https://course.fcu.edu.tw/Login.aspx':
        return False
    return response


def searchCourse(courseNum, rs, response, thisUrl, cookies, headers, params):
    # 解析響應頁面
    soup = BeautifulSoup(response.text, 'html.parser')
    # 提取 __VIEWSTATE 值
    viewstate = soup.select_one('#__VIEWSTATE')['value']
    # 提取 __EVENTVALIDATION 值
    eventvalidation = soup.select_one('#__EVENTVALIDATION')['value']

    data = {
        'ctl00_ToolkitScriptManager1_HiddenField': '',
        'ctl00_MainContent_TabContainer1_ClientState': '{"ActiveTabIndex":2,"TabState":[true,true,true]}',
        '__EVENTTARGET': 'ctl00$MainContent$TabContainer1$tabSelected$gvToAdd',
        '__EVENTARGUMENT': 'addCourse$0',
        '__LASTFOCUS': '',
        'ctl00_MainContent_TabContainer1_tabSelected_TabContainer2_ClientState': '{"ActiveTabIndex":0,"TabState":[true,true,true]}',
        '__VIEWSTATE': viewstate,
        '__VIEWSTATEGENERATOR': '02808545',
        '__VIEWSTATEENCRYPTED': '',
        '__EVENTVALIDATION': eventvalidation,
        'ctl00$MainContent$TabContainer1$tabCourseSearch$wcCourseSearch$ddlDegree': '1',
        'ctl00$MainContent$TabContainer1$tabCourseSearch$wcCourseSearch$ddlDept': '',
        'ctl00$MainContent$TabContainer1$tabCourseSearch$wcCourseSearch$ddlUnit': '',
        'ctl00$MainContent$TabContainer1$tabCourseSearch$wcCourseSearch$ddlClass': '',
        'ctl00$MainContent$TabContainer1$tabCourseSearch$wcCourseSearch$tbSubID': '',
        'ctl00$MainContent$TabContainer1$tabCourseSearch$wcCourseSearch$ddlWeek': '',
        'ctl00$MainContent$TabContainer1$tabCourseSearch$wcCourseSearch$ddlPeriod': '',
        'ctl00$MainContent$TabContainer1$tabCourseSearch$wcCourseSearch$tbCourseName': '',
        'ctl00$MainContent$TabContainer1$tabCourseSearch$wcCourseSearch$tbTeacherName': '',
        'ctl00$MainContent$TabContainer1$tabCourseSearch$wcCourseSearch$ddlUseLanguage': '01',
        'ctl00$MainContent$TabContainer1$tabCourseSearch$wcCourseSearch$ddlSpecificSubjects': '1',
        'ctl00$MainContent$TabContainer1$tabCourseSearch$wcCourseSearch$cbShowSelected': 'on',
        # 'ctl00$MainContent$TabContainer1$tabSelected$TabContainer2$genSubTab$gvPerSelGe$ctl02$geDropDownList': '1',
        # 'ctl00$MainContent$TabContainer1$tabSelected$TabContainer2$genSubTab$gvPerSelGe$ctl03$geDropDownList': '2',
        'ctl00$MainContent$TabContainer1$tabSelected$tbSubID': courseNum,
        'ctl00$MainContent$TabContainer1$tabSelected$btnGetSub': '查詢',
        'ctl00$MainContent$TabContainer1$tabSelected$cpeWishList_ClientState': 'true',
    }

    response = rs.post(thisUrl[:34] + "NetPreSelect.aspx", params=params, cookies=cookies, headers=headers, data=data)
    # response = rs.post(thisUrl[:34] + "AddWithdraw.aspx" + thisUrl[34:83], params=params, cookies=cookies, headers=headers, data=data)
    return addCourse(rs, response, thisUrl, cookies, headers, params)


def addCourse(rs, response, thisUrl, cookies, headers, params):
    soup = BeautifulSoup(response.text, 'html.parser')
    viewstate = soup.select_one('#__VIEWSTATE')['value']
    eventvalidation = soup.select_one('#__EVENTVALIDATION')['value']
    while 1:
        # if response_queue.qsize() > 100:
        #     continue
        data = {
            'ctl00_ToolkitScriptManager1_HiddenField': '',
            'ctl00_MainContent_TabContainer1_ClientState': '{"ActiveTabIndex":2,"TabState":[true,true,true]}',
            '__EVENTTARGET': 'ctl00$MainContent$TabContainer1$tabSelected$gvToAdd',
            '__EVENTARGUMENT': 'addCourse$0',
            '__LASTFOCUS': '',
            'ctl00_MainContent_TabContainer1_tabSelected_TabContainer2_ClientState': '{"ActiveTabIndex":1,"TabState":[true,true,true]}',
            '__VIEWSTATE': viewstate,
            '__VIEWSTATEGENERATOR': '02808545',
            '__VIEWSTATEENCRYPTED': '',
            '__EVENTVALIDATION': eventvalidation,
            'ctl00$MainContent$TabContainer1$tabCourseSearch$wcCourseSearch$ddlDegree': '1',
            'ctl00$MainContent$TabContainer1$tabCourseSearch$wcCourseSearch$ddlDept': '',
            'ctl00$MainContent$TabContainer1$tabCourseSearch$wcCourseSearch$ddlUnit': '',
            'ctl00$MainContent$TabContainer1$tabCourseSearch$wcCourseSearch$ddlClass': '',
            'ctl00$MainContent$TabContainer1$tabCourseSearch$wcCourseSearch$tbSubID': '',
            'ctl00$MainContent$TabContainer1$tabCourseSearch$wcCourseSearch$ddlWeek': '',
            'ctl00$MainContent$TabContainer1$tabCourseSearch$wcCourseSearch$ddlPeriod': '',
            'ctl00$MainContent$TabContainer1$tabCourseSearch$wcCourseSearch$tbCourseName': '',
            'ctl00$MainContent$TabContainer1$tabCourseSearch$wcCourseSearch$tbTeacherName': '',
            'ctl00$MainContent$TabContainer1$tabCourseSearch$wcCourseSearch$ddlUseLanguage': '01',
            'ctl00$MainContent$TabContainer1$tabCourseSearch$wcCourseSearch$ddlSpecificSubjects': '1',
            'ctl00$MainContent$TabContainer1$tabCourseSearch$wcCourseSearch$cbShowSelected': 'on',
            # 'ctl00$MainContent$TabContainer1$tabSelected$TabContainer2$genSubTab$gvPerSelGe$ctl02$geDropDownList': '1',
            # 'ctl00$MainContent$TabContainer1$tabSelected$TabContainer2$genSubTab$gvPerSelGe$ctl03$geDropDownList': '2',
        }

        response = rs.post(thisUrl[:34] + "NetPreSelect.aspx", params=params, cookies=cookies, headers=headers, data=data)
        # response = rs.post(thisUrl[:34] + "AddWithdraw.aspx" + thisUrl[34:83], params=params, cookies=cookies, headers=headers, data=data)
        
        # if response == None:
        #     return False
        soup = BeautifulSoup(response.text, 'html.parser')
        if (soup.select_one('#ctl00_MainContent_TabContainer1_tabSelected_lblMsgBlock') == None):
            return True
        if check(soup) == True:
            return True
        elif check(soup) == "登出":
            return False



def check(soup):
    
    if soup.select_one('#ctl00_MainContent_TabContainer1_tabSelected_lblMsgBlock').get_text() != "":
        if soup.select_one('#ctl00_MainContent_TabContainer1_tabSelected_lblMsgBlock span').get_text() == "退選成功":
            print(soup.select_one('#ctl00_MainContent_TabContainer1_tabSelected_lblMsgBlock').get_text())
            return True
        elif soup.select_one('#ctl00_MainContent_TabContainer1_tabSelected_lblMsgBlock span').get_text() == "加選成功":
            print(soup.select_one('#ctl00_MainContent_TabContainer1_tabSelected_lblMsgBlock').get_text())
            return True
        elif soup.select_one('#ctl00_MainContent_TabContainer1_tabSelected_lblMsgBlock span').get_text() == "選課代號重覆!!":
            print(soup.select_one('#ctl00_MainContent_TabContainer1_tabSelected_lblMsgBlock').get_text())
            return True
        elif soup.select_one('#ctl00_MainContent_TabContainer1_tabSelected_lblMsgBlock span').get_text() == "退選失敗, 請重新執行":
            print(soup.select_one('#ctl00_MainContent_TabContainer1_tabSelected_lblMsgBlock').get_text())
            return True
        elif soup.select_one('#ctl00_MainContent_TabContainer1_tabSelected_lblMsgBlock span').get_text() == "非進修部學生不可修習夜通識科目":
            print(soup.select_one('#ctl00_MainContent_TabContainer1_tabSelected_lblMsgBlock').get_text())
            return True
        elif soup.select_one('#ctl00_MainContent_TabContainer1_tabSelected_lblMsgBlock span').get_text() == "上課時間與其他課程衝堂":
            print(soup.select_one('#ctl00_MainContent_TabContainer1_tabSelected_lblMsgBlock').get_text())
            return True
        elif soup.select_one('#ctl00_MainContent_TabContainer1_tabSelected_lblMsgBlock span').get_text() == "預選科目至多30學分":
            print(soup.select_one('#ctl00_MainContent_TabContainer1_tabSelected_lblMsgBlock').get_text())
            return True
        elif soup.select_one('#ctl00_MainContent_TabContainer1_tabSelected_lblMsgBlock span').get_text() == "XX過度XX":
            return "登出"
    # 回傳沒有成功
    return False


def main():
    load_dotenv()
    username = os.getenv("USER_NAME")
    password = os.getenv("PASSWORD")

    while 1:
        rs = requests.session()
        rs.timeout = 5
        response = login(username, password, rs)
        if response == False:
            continue

        thisUrl = response.url
        cookies = rs.cookies
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Origin': thisUrl[:33],
            'Referer': thisUrl,
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
            'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
        }
            # 'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
        
        params = {
            'guid': thisUrl.split("guid=")[1].split("&")[0],
            'lang': 'zh-tw',
        }

        # response = searchCourse('0119', rs, response, thisUrl, cookies, headers, params)
        thread1 = threading.Thread(target=searchCourse, args=('2988', rs, response, thisUrl, cookies, headers, params))
        thread1.start()
        thread2 = threading.Thread(target=searchCourse, args=('0306', rs, response, thisUrl, cookies, headers, params))
        thread2.start()
        thread3 = threading.Thread(target=searchCourse, args=('0065', rs, response, thisUrl, cookies, headers, params))
        thread3.start()



        response = thread1.join()
        if response == False:
            rs.close()
            requests.get('https://course.fcu.edu.tw/')
            continue
        else:
            print("2988已完成")
        
        
        response = thread2.join()
        if response == False:
            rs.close()
            requests.get('https://course.fcu.edu.tw/')
            continue
        else:
            print("0306已完成")

        response = thread3.join()
        if response == False:
            rs.close()
            requests.get('https://course.fcu.edu.tw/')
            continue
        else:
            print("0065已完成")

        break
        
if __name__ == '__main__':
    main()



