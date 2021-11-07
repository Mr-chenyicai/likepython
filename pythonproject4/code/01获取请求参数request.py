from flask import Flask, request
app = Flask(__name__)
# 接口 api
@app.route('/index', methods=["GET", "POST"])
def index():
    # request中包含了前端发送过来的所有请求数据
    # 通过request.form可以直接提取请求体中的表单格式的数据，是一个类字典的对象
    # from 或者 data是从body请求体里拿到传参，args是从url中拿到传参
    name = request.form.get("name1")
    age = request.form.get("age1")
    city = request.args.get("city")
    return "hello xingming=%s ningling=%s city=%s" % (name, age, city)
if __name__ == '__main__':

    app.run(
        host="192.168.0.103",
        port="8080"
    )