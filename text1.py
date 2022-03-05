import pandas as pd
import requests
from bs4 import BeautifulSoup
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'
}


def parse():
    data = []  # 定义全局列表t
    data1 = []
    url = 'https://ncov.dxy.cn/ncovh5/view/pneumonia'  # url

    head_data = requests.get(url=url, headers=headers).content  # 获取数据
    res = BeautifulSoup(head_data, 'html.parser')  # 利用bs4解析数据
    res = res.find('script', {'id': 'getAreaStat'}).text  # 利用bs4获取国内的数据
    res = re.findall('try \{ window.getAreaStat = (.*)}catch', res, re.S)[0]  # 利用正则表达式先取得里面的所有数据
    res = re.findall('\{(.*?)]}', res)  # 利用正则表达式再去取每个省的数据
    for i in res:
        provinceName = re.findall('"provinceName":"(.*?)"', i)  # 取省份名
        cityName = re.findall('"cityName":"(.*?)"', i)  # 取城市名
        if len(cityName) == 0:  # 判断城市的长度是否为0
            cityName = provinceName  # 为零则把城市 = 省份 方便后面的保存
        else:
            cityName.insert(0, provinceName[0])  # 在城市列表最开始的位置插入省份名
        currentConfirmedCount = re.findall('"currentConfirmedCount":(.*?),', i)  # 取现有确诊
        confirmedCount = re.findall('"confirmedCount":(.*?),', i)  # 去取累计确诊
        curedCount = re.findall('"curedCount":(.*?),', i)  # 取累计治愈
        deadCount = re.findall('"deadCount":(.*?),', i)  # 取累计死亡

        for i in range(0, len(currentConfirmedCount)):  # 遍历存到列表t
            data.append({
                'provinceName': cityName[0],
                'cityName': cityName[i],
                'currentConfirmedCount': currentConfirmedCount[i],
                'confirmedCount': confirmedCount[i],
                'curedCount': curedCount[i],
                'deadCount': deadCount[i],
            })
        for i in range(0, len(currentConfirmedCount)):  # 遍历存到列表t
            data1.append({
                '省份': cityName[0],
                '城市': cityName[i],
                '现有确诊': currentConfirmedCount[i],
                '累计确诊': confirmedCount[i],
                '累计治愈': curedCount[i],
                '累计死亡': deadCount[i],
            })
    # print(pd.DataFrame(data1).to_string())
    # print(res)
    print(head_data)


parse()
# pd.DataFrame(data1).to_csv('demo/csv/丁香园国内疫情.csv', encoding='utf-8', index=False)
# pd.DataFrame(data).to_sql('xyyq', if_exists='replace', con=con, index=False)
# con.execute('ALTER TABLE xyyq ADD id INT(16) NOT NULL PRIMARY KEY AUTO_INCREMENT FIRST;') # 添加自增字段id
