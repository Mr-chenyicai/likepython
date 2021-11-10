import random
# 随机生成一个手机号码
def genrate_phone():
    phone = random.randint(10000000000, 99999999999)
    phone = '1{0}'.format(phone)
    print(phone)
    return phone
def haha():
    genrate_phone()
if __name__ == '__main__':
    # genrate_phone()
    haha()
