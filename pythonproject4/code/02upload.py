# from flask import Flask
# app = Flask(__name__)
# @app.route("upload", methods=["POST"])
# def index():
#     pass
# if __name__ == '__main__':
#     app.run()

# f = open("./1.txt", "wb")
# # 2.向文件写内容
# f.write("002")
# # 3.关闭文件
# f.close()

with open("./1.txt", "wb") as f:
    f.write("hello flask")