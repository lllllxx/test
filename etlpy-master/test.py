from etl import ETLTool

tool = ETLTool();
tool.LoadProject('project.xml', '数据清洗ETL-大众点评');
datas = tool.RefreshDatas();
for r in datas:
    print(r)
