import requests
import random
class Add_teacher(object):
# 随机生成一个手机号码
    def genrate_phone(self):
        phone = random.randint(10000000000, 99999999999)
        phone = '1{0}'.format(phone)
        return phone
# 用户登陆页 获取用户uid
    def get_userid(self):
        # 构建url
        # 构建请求头部
        url = 'https://test.meixiu.mobi/api/u/v1/user/login'
        header = {
            'authorization': 'Bearer eyJhbGciOiJIUzUxMiJ9.eyJqdGkiOiI0NTgwNTIyOTY3NzgwNTk3NzYiLCJzdWIiOiI0NTgwNTIyOTY3NzgwNTk3NzYiLCJpYXQiOjE1ODkzNzQ2NDMsImF1ZCI6InVzZXIiLCJleHAiOjE1OTgwMTQ2NDN9.VMeHKQHHOHb_9Hd764BjDGQwYLwHrgbavqHcvisKGeFu5ZWAFGckS60dkNVHo20x_tU8vGlnDS8AC97IKTBFEw',
        }
        # 构建请求数据
        data = {
            'mobile': self.genrate_phone(),
            'code': '1813',
            'channel': '12'
        }
        # 4.对请求的数据进行封装
        r = requests.post(url, data=data, headers=header)
        print(r.json())
        print(r.status_code)
        # print(r.request.headers)
        rst = r.json()
        print("用户id："+rst["payload"]["id"])
        return rst["payload"]["id"]
#  选择级别后，获取订单号
    def get_ordernumber(self,uid):
        url = "https://test.meixiu.mobi/api/o/v1/buy/distributeAndFission"
        header = {
            'authorization': 'Bearer eyJhbGciOiJIUzUxMiJ9.eyJqdGkiOiI0NTgwNTIyOTY3NzgwNTk3NzYiLCJzdWIiOiI0NTgwNTIyOTY3NzgwNTk3NzYiLCJpYXQiOjE1ODkzNzQ2NDMsImF1ZCI6InVzZXIiLCJleHAiOjE1OTgwMTQ2NDN9.VMeHKQHHOHb_9Hd764BjDGQwYLwHrgbavqHcvisKGeFu5ZWAFGckS60dkNVHo20x_tU8vGlnDS8AC97IKTBFEw',
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
        print("ub请求参数：" + str(data))
        r = requests.post(url=url, json=data, headers=header)
        print(r.json())
        print(r.status_code)
        # print(r.headers)
        res = r.json()
        return res['payload']['orderId']
#  添加老师
    def get_teacher(self):
        userid = self.get_userid()
        url = 'https://test.meixiu.mobi/api/wp/v1/weixinProgram/getUrlSchema?type=10&uid=655142451753598976&url=pages/launch/follow/index&orderIds=579727939407758555'
        # 构建请求头
        header = {
            'authorization': 'Bearer eyJhbGciOiJIUzUxMiJ9.eyJqdGkiOiI0NTgwNTIyOTY3NzgwNTk3NzYiLCJzdWIiOiI0NTgwNTIyOTY3NzgwNTk3NzYiLCJpYXQiOjE1ODkzNzQ2NDMsImF1ZCI6InVzZXIiLCJleHAiOjE1OTgwMTQ2NDN9.VMeHKQHHOHb_9Hd764BjDGQwYLwHrgbavqHcvisKGeFu5ZWAFGckS60dkNVHo20x_tU8vGlnDS8AC97IKTBFEw',
        }
        data = {
            "type": "10",
            "uid": userid,
            "url": "pages/launch/follow/index",
            "orderIds": self.get_ordernumber(userid)
        }
        # 对请求数据进行封装
        r = requests.get(url=url, json=data, headers=header)
        print(r.json())
        print(r.status_code)
        print(r.headers)




if __name__ == '__main__':
    add_teacher = Add_teacher()
    add_teacher.get_teacher()