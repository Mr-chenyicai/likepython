# 冒泡排序
li = [10,8,4,7,5]
for i in range(len(li)-1):  #遍历数组，每次确定一个最大值和n个数进行比较 需要（n）-1次冒泡
    for j in range(len(li)-1-i):  #遍历数组，每次进行冒泡得到一个最大数后，以此类推每次都会减去一个数
        if li[j] > li[j+1]:
            li[j], li[j+1] = li[j+1], li[j]
print(li)