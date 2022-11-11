#统计不同的三元组的分布情况,up down flat三种状态，2段，9种状态
#其中，认为平，有一个阈值，相差不多即可认为平
#先分析合法的

#可以对程序做一个调参的改进，选择合适阈值使得，分类尽可能准确率高，通过变化参数，分别算出不同阈值下，准确率最好的一个阈值
from collections import defaultdict

# from operator import le




        

asorg={}
f=open("../../graphdata/nodefeature/20220601node.txt")
line=f.readline()
while line:
    tmp=line.split("|")
    asorg[int(tmp[0])]=tmp[4]
    line=f.readline()

f.close()

# print(asorg[100])
#总共的情况


f=open("legitimate2022.txt")
legtripledict = defaultdict(int)
line=f.readline()
while line:
    tmp=line.split("|")
    a1=int(tmp[0])
    a2=int(tmp[1])
    a3=int(tmp[2])
    
    if a1 in asorg and a2 in asorg and a3 in asorg:
        if asorg[a1] == asorg[a2] and asorg[a1] != asorg[a3]:
            legtripledict[(1,1,0)]+=1
        elif asorg[a1] == asorg[a3] and asorg[a1] != asorg[a2]:
            legtripledict[(1,0,1)]+=1
        elif asorg[a2] == asorg[a3] and asorg[a1] != asorg[a3]:
            legtripledict[(0,1,1)]+=1
        elif asorg[a1] != asorg[a2] and asorg[a1] != asorg[a3]:
            legtripledict[(0,0,0)]+=1
        elif asorg[a1] == asorg[a2] and asorg[a1] == asorg[a3]:
            print("legitimate")
            print(a1,a2,a3,asorg[a1])
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
    
    if a1 in asorg and a2 in asorg and a3 in asorg:
        if asorg[a1] == asorg[a2] and asorg[a1] != asorg[a3]:
            illegtripledict[(1,1,0)]+=1
        elif asorg[a1] == asorg[a3] and asorg[a1] != asorg[a2]:
            illegtripledict[(1,0,1)]+=1
        elif asorg[a2] == asorg[a3] and asorg[a1] != asorg[a3]:
            illegtripledict[(0,1,1)]+=1
        elif asorg[a1] != asorg[a2] and asorg[a1] != asorg[a3]:
            illegtripledict[(0,0,0)]+=1
        elif asorg[a1] == asorg[a2] and asorg[a1] == asorg[a3]:
            illegtripledict[(1,1,1)]+=1
            print("illegitimate")
            print(a1,a2,a3,asorg[a1])
    line=f.readline()
f.close()

print("不合法的三元组的分布是")
print(illegtripledict)
# illegitimate
# 8359 43148 8359 ORG-ZM1-RIPE
# illegitimate
# 8359 25086 8359 ORG-ZM1-RIPE
# illegitimate
# 3908 7991 3561 CCL-534-ARIN
# BGPstream不准的证据，两边相同的AS



  

