import json
import requests

def sendmessage(message):
    url = 'https://oapi.dingtalk.com/robot/send?access_token=6b897f39f7d59f49f8e88ed9673f4e631e951118ccb50f5aa7a16a9cf81486c3'  # 钉钉机器人的webhook地址
    HEADERS = {
        "Content-Type": "application/json ;charset=utf-8 ",
        "Charset": "UTF-8",
    }
    message = message
    String_textMsg = {
        "msgtype": "text",
        "text": {"content": message},
        "at": {
            "atMobiles": [
                "13722980205"  # @群成员
            ],
            "isAtAll": 1 # @全体成员
        }
    }
    String_textMsg = json.dumps(String_textMsg)
    res = requests.post(url, data=String_textMsg, headers=HEADERS)
    print(res.text)


# if '__name__' == '__main__':
sendmessage('好好学习天天向上 一路向阳 不负时光')