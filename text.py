import pandas as pd
import requests
import json

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'
}


def yqday():
    url = 'https://api.inews.qq.com/newsqa/v1/query/inner/publish/modules/list?modules=statisGradeCityDetail,diseaseh5Shelf'
    data = json.loads(requests.post(url=url, headers=headers).content.decode())['data']
    x = data['statisGradeCityDetail']
    y = []
    for i in x:
        j = [i['province'] + i['city'], i['confirmAdd'], i['nowConfirm'], i['grade']]
        y.append(j)

    x = ['address', 'addqz', 'xyqz', 'fxqy']

    # 使用create_engine + pandas 快捷保存数据库
    df = pd.DataFrame(y, columns=x)
    print(df.to_string())
yqday()

    # df.to_sql('bentuxianyou31', if_exists='replace', con=con, index=False)
    # con.execute('ALTER TABLE bentuxianyou31 ADD id INT(16) NOT NULL PRIMARY KEY AUTO_INCREMENT FIRST;') # 添加自增字段id
    # with open('demo/data/中国疫情.json', 'w', encoding='utf-8') as f:
    #     f.write(json.dumps(data, ensure_ascii=False, indent=4))
    #
    # pd.DataFrame(y).to_csv('demo/csv/近31省市区现有本土病例.csv', index=False, encoding='utf-8', header=x)
    # # 使用create_engine + pandas 快捷保存数据库
