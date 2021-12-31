class Potato(object):
    def __init__(self):
        # status：状态是生的
        # total: 烧烤总时间
        self.status = "生的"
        self.total_time = 0
        self.name_list = []
    def cook(self, time):
        # 计算总时间
        self.total_time += time

        # 修改地瓜状态
        if self.total_time < 3:
            self.status = "生的"
        elif self.total_time < 6:
            self.status = "半生不熟"
        elif self.total_time < 8:
            self.status = "熟了"
        else:
            self.status = "烤糊了"
    def add(self, name):
        # 给地瓜添加调料
        self.name_list.append(name)
    def __str__(self):
        if self.name_list:
            return ("地瓜的状态是%s,烧烤总时间为%d,添加的调料有%s" % (self.status, self.total_time, self.name_list))
        else:
            return ("地瓜的状态是%s,烧烤总时间为%d,还没有添加调料" % (self.status, self.total_time))
potato = Potato()
print(potato)
potato.cook(10)
potato.add("芝麻酱")
print(potato)