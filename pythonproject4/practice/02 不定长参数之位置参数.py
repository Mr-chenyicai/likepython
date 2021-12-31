# 接收所有位置参数，返回一个元组
def user_info(*args):
    print(args)
user_info("小明", 20 ,"男")

# 传进的所有参数都会被args变量收集，它会根据传进参数的位置合并为一个元组（tuple），args是元组类型，这就是包裹位置传递


# 不定长参数之关键字参数
# 收集所有关键字参数，返回一个字典
def user_info(**kwargs):
    print(kwargs)
user_info(name = 'tom', age = 20, gender = "男")
