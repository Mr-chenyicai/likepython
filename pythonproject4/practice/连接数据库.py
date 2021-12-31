import pymysql
# 打开数据库连接
db = pymysql.connect(host="rm-bp1072nxkqxhi2afv.mysql.rds.aliyuncs.com",user="viptscn",password="he&2d1%$sezz!",database="viptest",charset="utf8")
# 使用cursor方法获取操作游标
cursor = db.cursor()
# 执行sql操作语句，编写sql查询语句
sql = "select mobile from shy_userinfo where username='zmy测'"
# 执行sql语句
cursor.execute(sql)
result = cursor.fetchall()
# 关闭数据库连接
cursor.close()
db.close()
print(result)