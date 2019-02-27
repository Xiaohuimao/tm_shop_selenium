import pymysql
import warnings
import readcfg
#打开数据库连接
class To_mysql():
    def __init__(self):
        #忽略警告
        warnings.filterwarnings("ignore")
        #获取数据库配置
        self.cfg=readcfg.Readcfg()
        self.serverip=self.cfg.get_database("ServerIP")
        self.dbname=self.cfg.get_database("DbName")
        self.dbpassword=self.cfg.get_database("Password")
        self.dbusername=self.cfg.get_database("UserName")
        #获取查询sql
        self.get_select_zj_price=self.cfg.get_sql("select_zj_price")
        self.get_select_user_kyprice=self.cfg.get_sql("select_user_kyprice")
        self.get_select_user_djprice=self.cfg.get_sql("select_user_djprice")
        self.get_select_store_allprice=self.cfg.get_sql("select_store_allprice")
        self.get_select_store_fcprice=self.cfg.get_sql("select_store_fcprice")
        self.db=pymysql.connect(self.serverip,self.dbname,self.dbpassword,self.dbusername)
#使用cursor()方法创建一个游标对象cursor
        self.cursor=self.db.cursor()
#使用execute()方法执行SQL查询
#查询组件金额
    def select_zj_price(self):
        self.db.ping(reconnect=True)
        self.cursor.execute(self.get_select_zj_price)
        self.db.commit()
        self.zj_price=self.cursor.fetchone()
        self.db.close()
        return self.zj_price[0]
#查询用户可用余额
    def select_user_kyprice(self):
        self.db.ping(reconnect=True)
        self.cursor.execute(self.get_select_user_kyprice)
        self.db.commit()
        self.user_kyprice=self.cursor.fetchone()
        self.db.close()
        return self.user_kyprice[0]
#查询用户冻结余额
    def select_user_djprice(self):
        self.db.ping(reconnect=True)
        self.cursor.execute(self.get_select_user_djprice)
        self.db.commit()
        self.user_djprice=self.cursor.fetchone()
        self.db.close()
        return self.user_djprice[0]
#查询商家总金额
    def select_store_allprice(self):
        self.db.ping(reconnect=True)
        self.cursor.execute(self.get_select_store_allprice)
        self.db.commit()
        self.store_allprice=self.cursor.fetchone()
        self.db.close()
        return self.store_allprice[0]
#查询商家扶持金
    def select_store_fcprice(self):
        self.db.ping(reconnect=True)
        self.cursor.execute(self.get_select_store_fcprice)
        self.db.commit()
        self.store_fcprice=self.cursor.fetchone()
        self.db.close()
        return self.store_fcprice[0]
#查询商家等级
    #def select_store_
#关闭游标
    def close_cursor(self):
        self.cursor.close()
#关闭数据库
    def close_mysql(self):
        self.db.close()
if __name__=="__main__":
    my=To_mysql()
    print(my.select_zj_price())
    print(my.select_store_allprice())
    print(my.select_store_fcprice())
    print(my.select_user_djprice())
    print(my.select_user_kyprice())