import numpy as num



def fun():
    file = open("number.txt", 'r')
    numStr = file.read()
    file.close()
    numList = numStr.split(' ')
    n = len(numList)
    result = num.random.randint(n)
    return numList[result]
if __name__=="__main__":

    print('抽中的是：'+fun())
    while(True):
        a=input("是否继续(是则输入1，否则输入其他)：")
        if a!='1':
            print("结束")
            exit()
        print('抽中的是：' + fun())


