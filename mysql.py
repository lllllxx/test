import pymysql


class Mysql_search():
    def __init__(self, ls_host, ls_user, ls_password, ls_db, ls_port=38965, ls_charset="utf8"):
        self.ls_host = ls_host
        self.ls_user = ls_user
        self.ls_password = ls_password
        self.ls_db = ls_db
        self.ls_port = ls_port
        self.ls_charset = ls_charset

        try:
            # self.conn = pymysql.connect(host="10.5.254.238",
            #                             user="root",
            #                             password="Inspur2021@#",
            #                             db="bigscreen",
            #                             port=38965,
            #                             charset="utf8")
            self.conn = pymysql.connect(host=ls_host,
                                        user=ls_user,
                                        password=ls_password,
                                        db=ls_db,
                                        port=ls_port,
                                        charset=ls_charset)

            self.cursor = self.conn.cursor()
        except pymysql.err as e:
            print("error" % e)

    def get_one(self, sql):
        self.sql = sql
        # sql = "select * from close_contact_source "
        self.cursor.execute(sql)
        # self.cursor.execute(sql, ('post',))
        # print(dir(self.cursor))
        # print(self.cursor.description)
        # 获取第一条查询结果，结果是元组
        rest = self.cursor.fetchone()
        # 处理查询结果，将元组转换为字典
        result = dict(zip([k[0] for k in self.cursor.description], rest))
        self.cursor.close()
        return result

    def get_all(self, sql):
        self.sql = sql
        # sql = "select * from close_contact_source "
        self.cursor.execute(sql)
        # self.cursor.execute(sql, ('post',))
        # 获取第一条查询结果，结果是元组
        rest = self.cursor.fetchall()
        # 处理查询结果，将元组转换为字典
        result = [dict(zip([k[0] for k in self.cursor.description], row)) for row in rest]
        self.cursor.close()
        return result

    def db_close(self):
        self.conn.close()

# if __name__ == '__main__':
#     obj = Mysql_search()
#     # result = obj.get_one()
#     # print(result)
#     # print(result['url'])
#     reslt = obj.get_all()
#     for item in reslt:
#         print(item)
#         print("-" * 10)
#     obj.db_close()
