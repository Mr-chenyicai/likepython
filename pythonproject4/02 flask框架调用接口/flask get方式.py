import pymysql
from flask import Flask, request, jsonify
app = Flask(__name__)
# 通过路由'test'路径，GET方式来访问接口
@app.route('/test',methods = ["GET"])
def calculate():
    a = request.args.get("sb", 0)
    # 打开数据库连接
    db = pymysql.connect(host="rm-bp1072nxkqxhi2afv.mysql.rds.aliyuncs.com", user="viptscn", password="he&2d1%$sezz!",database="viptest", charset="utf8")
    # 使用cursor方法获取操作游标
    cursor = db.cursor()
    # 执行sql操作语句，编写sql查询语句
    # sql = "select * from shy_userinfo where param = '%s'" % values['param']"
    sql = "select mobile from shy_userinfo where username =?"
    sql = sql.replace('?', '\'' + str(a) + '\'', 1)
    # sql = "select mobile from shy_userinfo where username ={0}".format(a)
    # sql = "select mobile from shy_userinfo where username ={0}"+str(a)
    print(sql)
    # 执行sql语句
    cursor.execute(sql)
    result = cursor.fetchall()
    # 关闭数据库连接
    cursor.close()
    db.close()
    print(result)
    res = {"result": result}
    return jsonify(content_type='application/json;charset=utf-8',
                   reason='success',
                   charset='utf-8',
                   status='200',
                   content=res,)

if __name__ == '__main__':
    app.run(host='192.168.126.209',
            threaded=True,
            debug=False,
            port=8080)