#统计不同的三元组的分布情况,up down flat三种状态，2段，9种状态
#其中，认为平，有一个阈值，相差不多即可认为平
#先分析合法的

#可以对程序做一个调参的改进，选择合适阈值使得，分类尽可能准确率高，通过变化参数，分别算出不同阈值下，准确率最好的一个阈值
from collections import defaultdict

# from operator import le
import pandas as pd

def getrir(asnum):
    #输入一个AS号码，返回这个号码所属的RIR
    for item in asdict:
        if '-' in item:
            a1=item.split('-')[0]
            a2=item.split('-')[1]
            if asnum >= int(a1) and asnum <=int(a2):
                return asdict[item]
        else:
            if asnum == int(item):
                return asdict[item]
        

asdict={}
df = pd.read_csv('../rir/as-numbers-1.csv',usecols=[0,1])

#自动会忽略表头
for index, row in df.iterrows():
    # print(index) # 输出每行的索引值
    # print(row[0],row[1])
    if 'Assigned' in row[1]:
        asdict[row[0]]=row[1].split(' ')[2]

# print(asdict)

df = pd.read_csv('../rir/as-numbers-2.csv',usecols=[0,1])

#自动会忽略表头
for index, row in df.iterrows():
    # print(index) # 输出每行的索引值
    # print(row[0],row[1])
    if 'Assigned' in row[1]:
        asdict[row[0]]=row[1].split(' ')[2]

print(getrir(1000))



#总共的情况


f=open("legitimate2022.txt")
legtripledict = defaultdict(int)
line=f.readline()
while line:
    tmp=line.split("|")
    a1=int(tmp[0])
    a2=int(tmp[1])
    a3=int(tmp[2])
    
    #1表示是教研网络，0表示不是
    if getrir(a1) == getrir(a2) and getrir(a1) != getrir(a3):
        legtripledict[(1,1,0)]+=1
    elif getrir(a1) == getrir(a3) and getrir(a1) != getrir(a2):
        legtripledict[(1,0,1)]+=1
    elif getrir(a2) == getrir(a3) and getrir(a1) != getrir(a3):
        legtripledict[(0,1,1)]+=1
    elif getrir(a1) != getrir(a2) and getrir(a1) != getrir(a3):
        legtripledict[(0,0,0)]+=1
    elif getrir(a1) == getrir(a2) and getrir(a1) == getrir(a3):
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
    
    #1表示是教研网络，0表示不是
    if getrir(a1) == getrir(a2) and getrir(a1) != getrir(a3):
        illegtripledict[(1,1,0)]+=1
    elif getrir(a1) == getrir(a3) and getrir(a1) != getrir(a2):
        illegtripledict[(1,0,1)]+=1
    elif getrir(a2) == getrir(a3) and getrir(a1) != getrir(a3):
        illegtripledict[(0,1,1)]+=1
    elif getrir(a1) != getrir(a2) and getrir(a1) != getrir(a3):
        illegtripledict[(0,0,0)]+=1
    elif getrir(a1) == getrir(a2) and getrir(a1) == getrir(a3):
        illegtripledict[(1,1,1)]+=1
    line=f.readline()
f.close()

print("不合法的三元组的分布是")
print(illegtripledict)



  

