# 选择级别页面，生成订单
import json
import urllib.request
import requests
from activity.uc import c_url
# 构建url
# 构建请求头部
def b_url(uid):
    url = "https://test.meixiu.mobi/api/o/v1/buy/distributeAndFission"
    header = {
        "authority": "test.meixiu.mobi",
        "method": "POST",
        "path": "/api/o/v1/buy/distributeAndFission",
        "scheme": "https",
        "accept": "application/json, text/plain, */*",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "zh-CN,zh;q=0.9",
        'authorization':'Bearer eyJhbGciOiJIUzUxMiJ9.eyJqdGkiOiI0NTgwNTIyOTY3NzgwNTk3NzYiLCJzdWIiOiI0NTgwNTIyOTY3NzgwNTk3NzYiLCJpYXQiOjE1ODkzNzQ2NDMsImF1ZCI6InVzZXIiLCJleHAiOjE1OTgwMTQ2NDN9.VMeHKQHHOHb_9Hd764BjDGQwYLwHrgbavqHcvisKGeFu5ZWAFGckS60dkNVHo20x_tU8vGlnDS8AC97IKTBFEw',
        "content-length":"337",
        "content-type": "application/json",
        "cookie": "sensorsdata2015jssdkcross=%7B%22%24device_id%22%3A%2217a6b72dfb8891-01c444f82af9a1-34657300-1296000-17a6b72dfb93d6%22%7D; Hm_lvt_7d55c4519b3356830007f457e886a2af=1625300329; xiaoxiongmeishu_toss=Bearer%20eyJhbGciOiJIUzUxMiJ9.eyJqdGkiOiI1Nzg5OTA2MDc2NDU2NzU1MjAiLCJzdWIiOiI1Nzg5OTA2MDc2NDU2NzU1MjAiLCJpYXQiOjE2MjkxODIzNDgsImF1ZCI6ImFkbWluIiwiZXhwIjoxNjM3ODIyMzQ4fQ.7naKR5lJH9Cf4Rim75svWjkGXpoKFqO62BNmnAiTH0fTWW-q9qxKHvTRF0KQmzj_Be3IDFDhvKIJGxO6QUVu-w; _ga=GA1.1.1634318221.1636184390; _gcl_au=1.1.1929213032.1636184390; Hm_lvt_8be5ad4522d2012a74d5226b6009bfbd=1636184389,1636353867,1636353913; Hm_lpvt_8be5ad4522d2012a74d5226b6009bfbd=1636353964; sa_jssdk_2015_test_meixiu_mobi=%7B%22distinct_id%22%3A%22G9sfZHDU45PiduR0NHIkfw%3D%3D%22%2C%22first_id%22%3A%2217a6b72dfb8891-01c444f82af9a1-34657300-1296000-17a6b72dfb93d6%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%7D; _ga_94D92RYV3N=GS1.1.1636353698.7.1.1636354008.0; _ga_SSTGC8SVMQ=GS1.1.1636353698.7.1.1636354008.0",
        "origin": "https://test.meixiu.mobi",
        "referer": "https://test.meixiu.mobi/ai-app-h5-activity-test/freeActivity/chooseLevel?channelId=12&type=ALONE&userId=655097902222049280&packagesId=613&sup=S1&rmb=0&channel=12",
        'sec-ch-ua': '"Google Chrome"; v="95", "Chromium";v="95", ";Not A Brand";v="99"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Mobile Safari/537.36',
    }
    # 构建请求数据
    data = {
        'addressId': '0',
        'appsubject': "ART_APP",
        'category': '0',
        'channel': "12",
        'clientFrom': "DEFAULT",
        'coinType': "RMB",
        'come': "",
        'couponUserId': '0',
        'grouponId': '0',
        'mergeOutTradeNo': "",
        'origin': "",
        'packagesId': "613",
        'posterId': '0',
        'sendId': '0',
        'spreadCode': "",
        'stage': "",
        'sup': "S1",
        'targetAccount': '0',
        'topicId': '21',
        'type': "ALONE",
        'userId': uid
    }
    # 对请求数据进行封装
    print("ub请求参数："+str(data))
    r = requests.post(url=url, json=data, headers=header)
    print(r.json())
    print(r.status_code)
    print(r.headers)
    res = r.json()
    return res['payload']['orderId']

if __name__ == '__main__':
    ordid= b_url()
    print("-------")
    # c_url(ordid)
