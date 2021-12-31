import requests

url = "http://www.baidu.com"
# 案例1
# 请求时带参数 params
params = {"id": 1001, "kw": "beijing"}
# 请求带参是params
r = requests.get(url, params=params)

print(r.url)
print(r.status_code)
print(r.text)

r = requests.get(url)
print("cookie信息为:", r.cookies)
# 通过键名获取响应cookies的值
print(r.cookies['BDORZ'])