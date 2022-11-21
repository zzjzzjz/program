


if __name__=="__main__":
    file=open("answer.txt",'r')
    text=file.read()
    file.close()
    text=text.split("\n")
    text2=[]
    for i in range(len(text)):
        for j in range(len(text)):
            if i+1==eval(text[j][0]):
                text2.append(text[i])
                break
    if len(text)!=len(text2):
        print("answer文件有误")
        exit()

    result=0
    for i in range(len(text2)):
        tmp={'A':eval(text2[i][2:4]),'B':eval(text2[i][5:7]),'C':eval(text2[i][8:10])}
        text2[i]=tmp
    answer=input("输入答案：")
    result=0
    if len(answer)>len(text2):
        print('输入过长')
        exit()
    for i in range(len(answer)):
        result=result+text2[i][answer[i]]
    print("总分是："+str(result))

