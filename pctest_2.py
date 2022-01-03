import json
import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("mysql+pymysql://root:Inspur2021%40%23@10.5.254.238:38965/mysql")
sql = 'delete from lx_fx'
file = r'D:\test.txt'
f = open(file, "r")
r = f.read()
f.close()

data = json.loads(r)
data_h = data['data']['highlist']
data_m = data['data']['middlelist']

# 展平数据
df = pd.json_normalize(data_m, meta=['city', 'county', 'province'], record_path='communitys', record_prefix='jd')
df_1 = pd.json_normalize(data_h, meta=['city', 'county', 'province'], record_path='communitys', record_prefix='jd')
df = df.rename(columns={'jd0': 'jd'})
df_1 = df_1.rename(columns={'jd0': 'jd'})
df['fx'] = df.apply(lambda x: '中风险', axis=1)
df_1['fx'] = df_1.apply(lambda x: '高风险', axis=1)
df.to_sql('lx_fx', engine, if_exists="append", index=False)
df_1.to_sql('lx_fx', engine, if_exists="append", index=False)
