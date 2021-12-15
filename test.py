from mysql import Mysql_search
# if __name__ == '__main__':
obj = Mysql_search()
sql = "select * from close_contact_source "
    # result = obj.get_one()
    # print(result)
    # print(result['url'])
reslt = obj.get_all(sql)
print(reslt)
for item in reslt:
    print(item)
    print("-" * 10)
obj.db_close()

