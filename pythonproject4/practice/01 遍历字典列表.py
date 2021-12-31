student = [
    {"name": "阿土"},
    {"name": "小美"}
]
# 在学员列表中找对应的学员
find_name = "阿土"
for stu_dict in student:
    print(stu_dict)
    if stu_dict['name'] == find_name:
        print("这个学员叫 %s " % find_name)
        break
else:
    print("没找到这个学员叫 %s" % find_name)
print("循环结束")
