# 添加老师页
import json
import urllib.request
import requests
# 构建url
def c_url(ordid,uid):
    url = 'https://test.meixiu.mobi/api/wp/v1/weixinProgram/getUrlSchema?type=10&uid=655142451753598976&url=pages/launch/follow/index&orderIds=579727939407758555'
    # 构建请求头
    header = {
        'authority': 'test.meixiu.mobi',
        'method': 'GET',
        'path': '/api/wp/v1/weixinProgram/getUrlSchema?type=10&uid=655142451753598976&url=pages%2Flaunch%2Ffollow%2Findex&orderIds=579727939407758555',
        'scheme': 'https',
        'accept': 'application/json, text/plain, */*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9',
        'authorization':'Bearer eyJhbGciOiJIUzUxMiJ9.eyJqdGkiOiI0NTgwNTIyOTY3NzgwNTk3NzYiLCJzdWIiOiI0NTgwNTIyOTY3NzgwNTk3NzYiLCJpYXQiOjE1ODkzNzQ2NDMsImF1ZCI6InVzZXIiLCJleHAiOjE1OTgwMTQ2NDN9.VMeHKQHHOHb_9Hd764BjDGQwYLwHrgbavqHcvisKGeFu5ZWAFGckS60dkNVHo20x_tU8vGlnDS8AC97IKTBFEw',
        'cookie': 'sensorsdata2015jssdkcross=%7B%22%24device_id%22%3A%2217a6b72dfb8891-01c444f82af9a1-34657300-1296000-17a6b72dfb93d6%22%7D; Hm_lvt_7d55c4519b3356830007f457e886a2af=1625300329; xiaoxiongmeishu_toss=Bearer%20eyJhbGciOiJIUzUxMiJ9.eyJqdGkiOiI1Nzg5OTA2MDc2NDU2NzU1MjAiLCJzdWIiOiI1Nzg5OTA2MDc2NDU2NzU1MjAiLCJpYXQiOjE2MjkxODIzNDgsImF1ZCI6ImFkbWluIiwiZXhwIjoxNjM3ODIyMzQ4fQ.7naKR5lJH9Cf4Rim75svWjkGXpoKFqO62BNmnAiTH0fTWW-q9qxKHvTRF0KQmzj_Be3IDFDhvKIJGxO6QUVu-w; _ga=GA1.1.1634318221.1636184390; _gcl_au=1.1.1929213032.1636184390; Hm_lvt_8be5ad4522d2012a74d5226b6009bfbd=1636184389,1636353867,1636353913; Hm_lpvt_8be5ad4522d2012a74d5226b6009bfbd=1636362082; sa_jssdk_2015_test_meixiu_mobi=%7B%22distinct_id%22%3A%22%2Bbqs01d5ydSZV%2Fd3RPCvdg%3D%3D%22%2C%22first_id%22%3A%2217a6b72dfb8891-01c444f82af9a1-34657300-1296000-17a6b72dfb93d6%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%7D; _ga_94D92RYV3N=GS1.1.1636357705.8.1.1636362138.0; _ga_SSTGC8SVMQ=GS1.1.1636357705.8.1.1636362138.0',
        'referer': 'https://test.meixiu.mobi/ai-app-h5-activity-test/freeActivity/addWxGroup?userId=655142451753598976&orderId=579727939407758555&followType=teacher&channelId=7049',
        'sec-ch-ua': '"Google Chrome";v="95", "Chromium";v="95", ";Not A Brand";v="99"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': "Android",
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Mobile Safari/537.36',
    }
    data = {
        "type": "10",
        "uid": uid,
        "url": "pages/launch/follow/index",
        "orderIds": ordid
    }
    # 对请求数据进行封装
    r = requests.get(url=url, json=data, headers=header)
    print(r.json())
    print(r.status_code)
    print(r.headers)
