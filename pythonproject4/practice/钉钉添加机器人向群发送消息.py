import urllib.request
import requests
import json
# 1.构建url  url为机器人的webhook
url = "https://oapi.dingtalk.com/robot/send?access_token=6b897f39f7d59f49f8e88ed9673f4e631e951118ccb50f5aa7a16a9cf81486c3"
# 2.构建请求头部
header = {
    "Content-Type": "appliaction/json",
    "Charset": "UTF-8",
}
# 3.构建请求数据
data = {
    "msgtype": "text",
    "text": {
        "content": "好好学习天天向上，你过来呀"},  # data为要传入发送的数据
    "at": {
        "isAtAll": True  # @全体成员（在此可设置@特定某人）
    }
}
# 4.对请求的数据进行json封装
sendData = json.dumps(data)
sendData = sendData.encode("utf-8")
request = urllib.request.Request(url=url, data=sendData, headers=header)

opener = urllib.request.urlopen(request)
print(opener.read())