class ENV:
    #testing envrionment
    url = "http://localhost:8000"
    # 自动化专用用户
    username = 'test123456'
    password = 'test123456'

class DBSql:
    """
    初始化时清楚数据sql语句
    清空：用户、购物订单信息
    并插入：测试用户test123456
    """
    sql_file = rf'D:\电子系统商城\daily_fresh_demo-master\db.sqlite3'
    sql_list = [
        'DELETE FROM df_order_orderdetailinfo',
        'DELETE FROM df_order_orderinfo',
        'DELETE FROM df_user_userinfo',
        'DELETE FROM df_cart_info',
        "INSERT INTO 'df_user_userinfo' VALUES ('46','test123456','fb343flsdjf34930958jkfds9890890890','sadfasdfasd@qq.com','','','','' )"
    ]