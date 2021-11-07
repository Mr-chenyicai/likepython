import json
import urllib.request
import requests
# 构建url
# 构建请求头部
url = 'https://test.meixiu.mobi/api/u/v1/user/login'
header = {
    # 'Content-Type': 'application/json, text/plain, */*',
    'authority': 'test.meixiu.mobi',
    'method': 'POST',
    'path': '/api/u/v1/user/login',
    'scheme': 'https',
    'accept': 'application/json, text/plain, */*',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9',
    'authorization': 'Bearer eyJhbGciOiJIUzUxMiJ9.eyJqdGkiOiI0NTgwNTIyOTY3NzgwNTk3NzYiLCJzdWIiOiI0NTgwNTIyOTY3NzgwNTk3NzYiLCJpYXQiOjE1ODkzNzQ2NDMsImF1ZCI6InVzZXIiLCJleHAiOjE1OTgwMTQ2NDN9.VMeHKQHHOHb_9Hd764BjDGQwYLwHrgbavqHcvisKGeFu5ZWAFGckS60dkNVHo20x_tU8vGlnDS8AC97IKTBFEw',
    'content-length': '73',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://test.meixiu.mobi',
    'referer': 'https://test.meixiu.mobi/ai-app-h5-activity-test/freeActivity?channelId=12',
    'sec-ch-ua': '"Google Chrome";v="95", "Chromium";v="95", ";Not A Brand";v="99"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Mobile Safari/537.36'


}
# 构建请求数据
data = {
    'mobile': '18812312312',
    'code': '1813',
    'channel': '12'
}
# 4.对请求的数据进行json封装
r = requests.post(url, data=data, headers=header)
print(r.json())
print(r.status_code)
print(r.request.headers)

