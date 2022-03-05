import yagmail
from imbox import Imbox
import time
import pandas as pd
import requests
import openpyxl

password = 'ERDX3mTyAtHFwJ2c'


# def get_verse():
#     url = 'https://v2.jinrishici.com/one.json?client=browser-sdk/'
#     response = requests.get(url)
#     return f'您要的每日诗句为：{response.json()["data"]["content"]}'


def get_data(id):
    headers = {
        'Connection': 'keep-alive',
        'Authorization': 'Basic c3lzYWRtaW4tcmVhbG06Tm1nLkluc3B1ckAwOTI5',
        'Accept': 'text/plain, */*; q=0.01',
        'kbn-version': '6.8.2',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36',
        'Content-Type': 'application/json',
        'Origin': 'http://59.196.255.44:5601',
        'Referer': 'http://59.196.255.44:5601/app/kibana',
        'Accept-Language': 'zh-CN,zh;q=0.9',
    }

    params = (
        ('path', '/jkda/HS_HSJCSJ/_search'),
        ('method', 'POST'),
    )

    data = '{\r\n  "query": {\r\n    "bool": {\r\n      "must": [\r\n        {\r\n          "bool": {\r\n            "filter": {\r\n              "terms": {\r\n                "CARD_ID": ["' + id + '"]\r\n              }\r\n            }\r\n          }\r\n        }\r\n      ]\r\n    }\r\n  }\r\n}\n'

    response = requests.post('http://59.196.255.44:5601/api/console/proxy', headers=headers, params=params,
                             data=data,
                             verify=False)
    # return response.text

    response_dict = response.json()
    data = response_dict['hits']['hits']
    return data


# def get_weather(city):
#     url = f'http://wthrcdn.etouch.cn/weather_mini?city={city}'
#     response = requests.get(url).json()
#     results = response['data']['forecast'][0]
#     return f'{city}今天的天气情况为{results["type"]}，{results["high"][:-1]}度，{results["low"][:-1]}度'


def send_mail(email, results):
    mail = yagmail.SMTP(user='inspurhs@88.com', password=password, host='smtp.88.com')
    contents = [results]
    mail.send(email, '【自动回复】您要的信息见正文', contents, ["结果.xlsx"])


def job(a=1):
    global hf
    imbox = Imbox('imap.88.com', 'inspurhs@88.com', password, ssl=True)
    unread_inbox_messages = imbox.messages(unread=True)  # 获取未读邮件
    for uid, message in unread_inbox_messages:
        title = message.subject
        email = message.sent_from[0]['email']
        results = '附件'
        body = ','.join(a for a in message.body['plain'])
        body = body.split(",")
        # body = message.body['plain']
        # if title == '来句诗':
        #     results = get_verse()
        # if title[-2:] == '天气':
        #     results = get_weather(title[:-2])
        if title == '查询':
            for i in body:
                data = get_data(i)
                df = pd.json_normalize(data, meta=['DEPT_NAME', 'CHECK_RESULT', 'CARD_ID', 'NAME', 'CHECK_REPORT_TIME'])

                if a == 1:
                    hf = df
                else:
                    hf = hf.append(df)
                a += 1
        hf.to_excel('结果.xlsx', index=False)
        if results:
            send_mail(email, results)
        imbox.mark_seen(uid)


while True:
    job()
    time.sleep(60)
