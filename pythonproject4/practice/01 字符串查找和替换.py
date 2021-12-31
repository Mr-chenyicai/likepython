hello_str = 'hello world'
# 1.判断是否以指定字符串开始
print(hello_str.startswith("hello"))
# 2.判断是否以指定字符串结束
print(hello_str.endswith("world"))
# 3.查找指定字符串
print(hello_str.find("llo"))
# 4.替换字符串
# replace方法执行完成后，会返回一个新的字符串
# 注意：不会修改原有字符串内容
print(hello_str.replace("world", "python"))
print(hello_str)
