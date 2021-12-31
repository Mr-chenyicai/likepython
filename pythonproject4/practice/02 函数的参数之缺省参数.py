# 缺省参数也叫默认参数，用于定义函数，为参数提供默认值，调用函数时可不传该默认参数的值

def user_info(name, age, gender="男"):
    print(f"您的姓名是{name},年龄是{age},性别是{gender}")
user_info("Tom", "20")