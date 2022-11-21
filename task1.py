def compare(file1,file2):
    if file1 == file2:
        return -1
    else:
        if len(file1)<=len(file2):#file1长度小
            for i in range(len(file1)):
                if file1[i]!=file2[i]:
                    return i+1
        else:
            for i in range(len(file2)):
                if file2[i]!=file1[i]:
                    return i+1


if __name__=="__main__":
    file1Name=input("文件1名：")
    file2Name = input("文件2名：")
    try:
        file1=open(file1Name,'r')
        file2=open(file2Name,'r')
        file1Str=file1.read()
        file2Str=file2.read()
        file1.close()
        file2.close()
    except:
        print('输入有误')
        exit()
    result=compare(file1Str,file2Str)
    if result==-1:
        print('No difference')
    else:
        print(str(result)+'处有问题')

