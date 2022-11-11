#统计不同的三元组的分布情况,up down flat三种状态，2段，9种状态
#其中，认为平，有一个阈值，相差不多即可认为平
#先分析合法的

#可以对程序做一个调参的改进，选择合适阈值使得，分类尽可能准确率高，通过变化参数，分别算出不同阈值下，准确率最好的一个阈值
from collections import defaultdict

# from operator import le




        

ascountry={}
f=open("../../graphdata/nodefeature/20220601node.txt")
line=f.readline()
while line:
    tmp=line.split("|")
    ascountry[int(tmp[0])]=tmp[7]
    line=f.readline()

f.close()

print(ascountry[100])
#总共的情况


f=open("legitimate2022.txt")
legtripledict = defaultdict(int)
line=f.readline()
while line:
    tmp=line.split("|")
    a1=int(tmp[0])
    a2=int(tmp[1])
    a3=int(tmp[2])
    
    if a1 in ascountry and a2 in ascountry and a3 in ascountry:
        if ascountry[a1] == ascountry[a2] and ascountry[a1] != ascountry[a3]:
            legtripledict[(1,1,0)]+=1
        elif ascountry[a1] == ascountry[a3] and ascountry[a1] != ascountry[a2]:
            legtripledict[(1,0,1)]+=1
        elif ascountry[a2] == ascountry[a3] and ascountry[a1] != ascountry[a3]:
            legtripledict[(0,1,1)]+=1
        elif ascountry[a1] != ascountry[a2] and ascountry[a1] != ascountry[a3]:
            legtripledict[(0,0,0)]+=1
        elif ascountry[a1] == ascountry[a2] and ascountry[a1] == ascountry[a3]:
            legtripledict[(1,1,1)]+=1
    line=f.readline()
f.close()
print("合法的三元组的分布是")
print(legtripledict)

#在分析不合法的
illegtripledict = defaultdict(int)
f=open("illegitimate2022.txt")
line=f.readline()
while line:
    tmp=line.split("|")
    a1=int(tmp[0])
    a2=int(tmp[1])
    a3=int(tmp[2])
    
    if a1 in ascountry and a2 in ascountry and a3 in ascountry:
        if ascountry[a1] == ascountry[a2] and ascountry[a1] != ascountry[a3]:
            illegtripledict[(1,1,0)]+=1
        elif ascountry[a1] == ascountry[a3] and ascountry[a1] != ascountry[a2]:
            illegtripledict[(1,0,1)]+=1
        elif ascountry[a2] == ascountry[a3] and ascountry[a1] != ascountry[a3]:
            illegtripledict[(0,1,1)]+=1
        elif ascountry[a1] != ascountry[a2] and ascountry[a1] != ascountry[a3]:
            illegtripledict[(0,0,0)]+=1
        elif ascountry[a1] == ascountry[a2] and ascountry[a1] == ascountry[a3]:
            illegtripledict[(1,1,1)]+=1
    line=f.readline()
f.close()

print("不合法的三元组的分布是")
print(illegtripledict)



  

