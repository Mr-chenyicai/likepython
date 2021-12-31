class Furniture(object):
    def __init__(self, name, area):
        # 家具的类型
        self.name = name
        # 家具的面积
        self.area = area
    def __str__(self):
        return ("家具的类型是%s,家具的面积是%d" % (self.name, self.area))


class House(object):
    def __init__(self, adress, area):
        self.adress = adress
        self.h_area = area
        self.furniture_list = []
        self.free_area = area
    def add_furniture(self, obj_furniture):
        """添加家具  obj_furniture:家具类的对象"""
        pass








bed = Furniture("豪华双人床", 15)
print(bed)
