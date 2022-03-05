import requests
import pandas as pd

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

        response = requests.post('http://59.196.255.44:5601/api/console/proxy', headers=headers, params=params, data=data,
                                 verify=False)
            # return response.text

        response_dict = response.json()
        data = response_dict['hits']['hits']
        return data

a=get_data('150203199411250316')
b=get_data('150403199912301020')

df_a = pd.json_normalize(a, meta=['DEPT_NAME', 'CHECK_RESULT', 'CARD_ID', 'NAME', 'CHECK_REPORT_TIME'])
df_b = pd.json_normalize(b, meta=['DEPT_NAME', 'CHECK_RESULT', 'CARD_ID', 'NAME', 'CHECK_REPORT_TIME'])


df_a = df_a.append(df_b)
df_a.to_excel('结果.xlsx')