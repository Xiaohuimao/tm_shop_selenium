import pymysql
import warnings

#打开数据库连接
class To_mysql():
    def __init__(self):
        #忽略警告
        warnings.filterwarnings("ignore")
        self.db=pymysql.connect("47.104.165.114","shop_360tian_com","jX53ipbEE67R7wNT","shop_360tian_com")
#使用cursor()方法创建一个游标对象cursor
        self.cursor=self.db.cursor()
#使用execute()方法执行SQL查询
#查询组件金额
    def select_zj_price(self):
        self.db.ping(reconnect=True)
        self.cursor.execute("select price from tm_spec_goods_price_approval where goods_approval_id=335")
        self.db.commit()
        self.zj_price=self.cursor.fetchone()
        self.db.close()
        return self.zj_price[0]
#查询用户可用余额
    def select_user_kyprice(self):
        self.db.ping(reconnect=True)
        self.cursor.execute("select user_money from tm_users where mobile=17623250366")
        self.db.commit()
        self.user_kyprice=self.cursor.fetchone()
        self.db.close()
        return self.user_kyprice[0]
#查询用户冻结余额
    def select_user_djprice(self):
        self.db.ping(reconnect=True)
        self.cursor.execute("select frozen_money from tm_users where mobile=17623250366")
        self.db.commit()
        self.user_djprice=self.cursor.fetchone()
        self.db.close()
        return self.user_djprice[0]
#查询商家总金额
    def select_store_allprice(self):
        self.db.ping(reconnect=True)
        self.cursor.execute("select store_money from tm_store where user_name=17623250366")
        self.db.commit()
        self.store_allprice=self.cursor.fetchone()
        self.db.close()
        return self.store_allprice[0]
#查询商家扶持金
    def select_store_fcprice(self):
        self.db.ping(reconnect=True)
        self.cursor.execute("select store_money_support from tm_store where user_name=17623250366")
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