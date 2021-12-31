# xiaoming_dict = {"name": "小明"}
# # 1.取值
# print(xiaoming_dict["name"])
# # 2.增加/修改
# # 如果key不存在，会新增键值对
# xiaoming_dict["age"] = 18
# # 如果key存在，会修改已经存在的键值对
# xiaoming_dict["name"] = "xiaoxiaoming"
# # 3.删除
# xiaoming_dict.pop("name")
# print(xiaoming_dict)

xiaoming_dict = {"name": "小明", "age": 18}
# 统计键值对数量
print(len(xiaoming_dict))
# 合并字典
temp_dict = {"height": "1.75", "age": 20}
xiaoming_dict.update(temp_dict)
print(xiaoming_dict)
