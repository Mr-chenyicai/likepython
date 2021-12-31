# 定义两个函数
# 函数一 有返回值50  函数二把返回值50作为参数传递（定义函数二有形参）

def test1():
    return 50

def test2(num):
    print(num)

result = test1()
# 将test1函数返回的值赋值给变量result
# print(result)
test2(result)