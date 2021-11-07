from flask import Flask,redirect,url_for
app = Flask(__name__)
@app.route('/')
def index():
    """定义视图函数"""
    return 'hello word'

"""方法一"""
# 通过redirect添加url来直接访问此网址
# @app.route('/login')
# def login():
#     url = 'https://blog.csdn.net/birdflyinhigh/article/details/79559425?utm_source=blogxgwz5'
#     return redirect(url)
"""方法二"""
# "url_for反解析"，，通过使用url_for的函数，通过视图函数的名字找到视图对应的url路径

@app.route('/login')
def login():
    url = url_for("index")

if __name__ == '__main__':
    app.run(
        host="192.168.126.209",
        port="8080"
    )