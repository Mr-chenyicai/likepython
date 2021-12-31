import random
# 随机生成一个手机号码
def genrate_phone():
    phone = random.randint(10000000000, 99999999999)
    phone = '1{0}'.format(phone)
    print(phone)
    return phone
def haha():
    for i in range(10):
        print(i)

    genrate_phone()
if __name__ == '__main__':
    haha()
name = "张三"

# def sum2(num1,num2):
#     result = num1+num2
#     print("求他们两个数的和为：%d + %d = %d" % (num1, num2, result))
# sum2(10,20)
#
# def print_line(char):
#     print(char * 100)
# print_line('=')