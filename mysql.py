# 获取连接方法
import pymysql


class DB:

    # 获取连接方法
    def get_db_conn(self, ls_host, ls_user, ls_password, ls_db, ls_port=38965, ls_charset="utf8"):
        self.ls_host = ls_host
        self.ls_user = ls_user
        self.ls_password = ls_password
        self.ls_db = ls_db
        self.ls_port = ls_port
        self.ls_charset = ls_charset
        conn = pymysql.connect(host=ls_host,
                               user=ls_user,
                               password=ls_password,
                               db=ls_db,
                               port=ls_port,
                               charset=ls_charset)  # 如果查询有中文，需要指定测试集编码

        return conn

    # 封装数据库查询操作
    def query_db(self, sql):
        conn = self.get_db_conn()  # 获取连接
        cur = conn.cursor()  # 建立游标
        cur.execute(sql)  # 执行sql
        result = cur.fetchall()  # 获取所有查询结果
        cur.close()  # 关闭游标
        conn.close()  # 关闭连接
        return result  # 返回结果

    # 封装更改数据库操作
    def change_db(self, sql):
        conn = self.get_db_conn()  # 获取连接
        cur = conn.cursor()  # 建立游标
        try:
            cur.execute(sql)  # 执行sql
            conn.commit()  # 提交更改
        except Exception as e:
            conn.rollback()  # 回滚
        finally:
            cur.close()  # 关闭游标
            conn.close()  # 关闭连接

    # 封装常用数据库操作
    def check_user(self, name):
        # 注意sql中''号嵌套的问题
        sql = "select * from user where name = '{}'".format(name)
        result = self.query_db(sql)
        return True if result else False

    def add_user(self, name, password):
        sql = "insert into user (name, passwd) values ('{}','{}')".format(name, password)
        self.change_db(sql)

    def del_user(self, name):
        sql = "delete from user where name='{}'".format(name)
        self.change_db(sql)
