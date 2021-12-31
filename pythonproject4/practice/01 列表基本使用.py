name_List = ['zhangsan', 'lisi', 'wangwu']
# 1.取值和取索引
# 取值
print(name_List[2])
# 取索引               索引：知道数据的内容，想确定数据在列表中的位置
print(name_List.index('wangwu'))

# 2.修改
name_List[1] = "李四"

# 3.增加
# append方法可以向列表的末尾追加数据
name_List.append("zhaoliu")
# insert方法可以在列表的指定索引位置插入数据
name_List.insert(1, "王桑")
# extend 方法可以把其他列表的完整内容，追加到当前列表的末尾
temp_list = ['孙悟空', '猪八戒']
name_List.extend(temp_list)

# 4.删除
# remove可以从列表中删除指定的数据
name_List.remove("猪八戒")
# pop方法可以默认删除列表最后一个数据
name_List.pop()
# pop方法可以指定要删除元素的索引
name_List.pop(3)
print(name_List)