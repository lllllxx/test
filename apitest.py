import json
from flask_cors import *
from mysql import *
from flask import Flask, request
from gevent import pywsgi
server = Flask(__name__)


@server.route('/index1', methods=['POST'])
def index1():
    res = {'msg': 'my first interface', 'msg_code': 0}
    return json.dumps(res, ensure_ascii=False)



# conn = cx_Oracle.connect('abc/abd@192.168.123.456/data123')
# cur = conn.cursor()
# sql = "SELECT XXNAME,XXCLASS,XXNUMBER,XXSCORE FROM TEST123 where rownum<5"
# cur.execute(sql)
# data = cur.fetchall()
# # print(data)
# para = []
# for i in data:
#     text = {'name': i[0], 'class': i[1], 'number': i[2], 'score': i[3]}
#     # print(text)
#     para.append(text)
# return json.dumps(para, ensure_ascii=False, indent=4)


if __name__ == '__main__':
    server = pywsgi.WSGIServer(('0.0.0.0', 7777), server)
    server.serve_forever()


# ---------------------------------------------------------------------
# # -*- coding: UTF-8 -*-
# import cx_Oracle
# import os
# import json
# from flask_cors import *
#
# os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
# from flask import Flask, request
#
# app = Flask(__name__)
#
#
# @app.route('/index1', methods=['POST'])
# def indextest():
#     inputData = request.json.get('inputData')
#     data1 = getcontent(inputData)
#     return data1
#
#
# def getcontent(inputData):
#     conn = cx_Oracle.connect('abc/abd@192.168.123.456/data123')  # 连自己的数据库
#     cur = conn.cursor()
#     sql = "SELECT XXNAME,XXCLASS,XXNUMBER,XXSCORE FROM TEST123 where XXNAME='%s'" % (inputData)
#     cur.execute(sql)
#     data = cur.fetchone()
#     print(data)
#     result = {'name': data[0], 'class': data[1], 'number': data[2], 'score': data[3]}
#     return json.dumps(result, ensure_ascii=False, indent=4)
#
#
# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5590)
