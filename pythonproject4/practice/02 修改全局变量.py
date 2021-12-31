a = 100
def testA():
    print(a)

def testB():
    print(a)

def testC():
    # global关键字 声明a是全局变量
    global a
    a = 200
    print(a)
testA()
testB()
testC()
