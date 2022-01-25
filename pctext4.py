import json
import pandas as pd
from sqlalchemy import create_engine
import requests

engine = create_engine("mysql+pymysql://root:Inspur2021%40%23@10.5.254.238:38965/mysql")
sql = 'delete from lx_fx'
cursor = engine.execute(sql)

r = requests.get('https://diqu.gezhong.vip/api.php')
data = r.json()
# print(data)
data_h = data['data']['highlist']
data_m = data['data']['middlelist']
data_t = data['data']['end_update_time']
# print(data_h)
# print(data_m)
# print(data_t)

#
# # 展平数据
df_m = pd.json_normalize(data_m, meta=['city', 'county', 'province'], record_path='communitys', record_prefix='jd')
df_h = pd.json_normalize(data_h, meta=['city', 'county', 'province'], record_path='communitys', record_prefix='jd')
# 换列名
df_m = df_m.rename(columns={'jd0': 'jd'})
df_h = df_h.rename(columns={'jd0': 'jd'})
# 增加风险字段、日期
df_m['fx'] = df_m.apply(lambda x: '中风险', axis=1)
df_h['fx'] = df_h.apply(lambda x: '高风险', axis=1)
# df_m['create_time'] = df_m.apply(lambda x: data_t[0:9], axis=1)
# df_h['create_time'] = df_h.apply(lambda x: data_t[0:9], axis=1)
df_m.insert(0, 'create_time', data_t[0:9])
df_h.insert(0, 'create_time', data_t[0:9])

df_m.to_sql('lx_fx', engine, if_exists="append", index=False)
df_h.to_sql('lx_fx', engine, if_exists="append", index=False)
