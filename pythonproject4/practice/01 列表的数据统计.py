name_list = ["张三", "李四", "王五", "赵六", "赵六"]
# len（length长度）函数可以统计列表中元素的总数
for my_name in name_list:
    print("我的名字叫 %s" % my_name)
result = len(name_list)
print("列表中有 %d 个人" % result)
# count 可以统计列表中某一个元素出现的次数
count = name_list.count("赵六")
print("列表中赵六出现了 %d 次" % count)


num_list = [6, 3, 9, 10, 7, 8]
# 升序排列
num_list.sort()
print(num_list)
# 降序排列
num_list.sort(reverse=True)
print(num_list)
# 反转排序
num_list.reverse()
print(num_list)