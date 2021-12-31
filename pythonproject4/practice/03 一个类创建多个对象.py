# 1.一个类创建多个对象的时候
# 2.多个对象都调用函数的时候，self地址是否相同
# class Washer():
#     def wash(self):
#         print("洗衣服")
#         print(self)
# haier1 = Washer()
# haier1.wash()
#
# haier2 = Washer()
# haier2.wash()

# 小明爱跑步
class Person():
    def __init__(self, name, weight):
        # self.属性 = 形参
        self.name = name
        self.weight = weight
    def __str__(self):
        return "我的名字叫 %s 体重是 %d" % (self.name, self.weight)
    def run(self):
        pass
    def eat(self):
        pass
Xiaoming = Person("小明", 70)
Xiaoming.run()
print(Xiaoming)

Xiaomei = Person("小美", 50)
print(Xiaomei)
