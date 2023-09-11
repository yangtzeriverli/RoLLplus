#统计不同的三元组的分布情况,up down flat三种状态，2段，9种状态
#其中，认为平，有一个阈值，相差不多即可认为平
#先分析合法的

#可以对程序做一个调参的改进，选择合适阈值使得，分类尽可能准确率高，通过变化参数，分别算出不同阈值下，准确率最好的一个阈值
# from collections import defaultdict
# from operator import le

# 先分析合法的三元组的特征，先是2021年的
# flatthrehold=0
# legsum=0
# legtripledict = defaultdict(int)
# f=open("legitimatedegree2022.txt")
# 以前加了个中间的过度，先把度存储到一个文件中

legtripletlist=[]

clusteringcoefficient21={}
# 只有2023年的数据
f=open("clusteringcoefficient2021.txt")
line=f.readline()
while line:
    tmp=line.split("|")
    clusteringcoefficient21[int(tmp[0])] = eval(tmp[1])
    # 这里不用tmp[0]字符串，而用int类型是因为后面的三元组文件中，最后一个tmp[2]是带有\n的，变成证书可以去掉
    line=f.readline()
f.close()

f=open("/home/jiang/data/routeleak/event/csv/legitimate.txt")
line=f.readline()
while line:
    tmp=line.split("|")
    if int(tmp[0]) in clusteringcoefficient21 and int(tmp[1]) in clusteringcoefficient21 and int(tmp[2]) in clusteringcoefficient21:
        a1=clusteringcoefficient21[int(tmp[0])]
        a2=clusteringcoefficient21[int(tmp[1])]
        a3=clusteringcoefficient21[int(tmp[2])]
        if a2!= 0:
            legtripletlist.append((a1+a3)/a2)
        # print(legsum)
    line=f.readline()
f.close()


# 22年的平均邻居度
clusteringcoefficient22={}
# 只有2023年的数据
f=open("clusteringcoefficient2022.txt")
line=f.readline()
while line:
    tmp=line.split("|")
    clusteringcoefficient22[int(tmp[0])] = eval(tmp[1])
    # 这里不用tmp[0]字符串，而用int类型是因为后面的三元组文件中，最后一个tmp[2]是带有\n的，变成证书可以去掉
    line=f.readline()
f.close()

f=open("/home/jiang/data/routeleak/event/csv/legitimate2022.txt")
line=f.readline()
while line:
    tmp=line.split("|")
    if int(tmp[0]) in clusteringcoefficient22 and int(tmp[1]) in clusteringcoefficient22 and int(tmp[2]) in clusteringcoefficient22:
        a1=clusteringcoefficient22[int(tmp[0])]
        a2=clusteringcoefficient22[int(tmp[1])]
        a3=clusteringcoefficient22[int(tmp[2])]
        if a2!= 0:
            legtripletlist.append((a1+a3)/a2)
    line=f.readline()
f.close()


# 23年的平均邻居度
clusteringcoefficient23={}
# 只有2023年的数据
f=open("clusteringcoefficient2023.txt")
line=f.readline()
while line:
    tmp=line.split("|")
    clusteringcoefficient23[int(tmp[0])] = eval(tmp[1])
    # 这里不用tmp[0]字符串，而用int类型是因为后面的三元组文件中，最后一个tmp[2]是带有\n的，变成证书可以去掉
    line=f.readline()
f.close()

f=open("/home/jiang/data/routeleak/event/csv/legitimate2023.txt")
line=f.readline()
while line:
    tmp=line.split("|")
    if int(tmp[0]) in clusteringcoefficient23 and int(tmp[1]) in clusteringcoefficient23 and int(tmp[2]) in clusteringcoefficient23:
        a1=clusteringcoefficient23[int(tmp[0])]
        a2=clusteringcoefficient23[int(tmp[1])]
        a3=clusteringcoefficient23[int(tmp[2])]
        if a2!= 0:
            legtripletlist.append((a1+a3)/a2)
    line=f.readline()
f.close()

# 最终输出全部的合法三元组的分布
# print("合法的三元组的分布是")
f=open("clusteringcoefficientdifferenceanalysisleg.txt",'w')
for item in legtripletlist:
    f.write(str(item)+'\n')
f.close()


# #在分析不合法的
# illegsum=0
# illegtripledict = defaultdict(int)
illegtripletlist=[]

f=open("/home/jiang/data/routeleak/event/csv/illegitimate.txt")
line=f.readline()
while line:
    tmp=line.split("|")
    if int(tmp[0]) in clusteringcoefficient21 and int(tmp[1]) in clusteringcoefficient21 and int(tmp[2]) in clusteringcoefficient21:
        a1=clusteringcoefficient21[int(tmp[0])]
        a2=clusteringcoefficient21[int(tmp[1])]
        a3=clusteringcoefficient21[int(tmp[2])]
        if a2!= 0:
            illegtripletlist.append((a1+a3)/a2)
    line=f.readline()
f.close()


f=open("/home/jiang/data/routeleak/event/csv/illegitimate2022.txt")
line=f.readline()
while line:
    tmp=line.split("|")
    if int(tmp[0]) in clusteringcoefficient22 and int(tmp[1]) in clusteringcoefficient22 and int(tmp[2]) in clusteringcoefficient22:
        a1=clusteringcoefficient22[int(tmp[0])]
        a2=clusteringcoefficient22[int(tmp[1])]
        a3=clusteringcoefficient22[int(tmp[2])]
        if a2!= 0:
            illegtripletlist.append((a1+a3)/a2)
    line=f.readline()
f.close()


f=open("/home/jiang/data/routeleak/event/csv/illegitimate2023.txt")
line=f.readline()
while line:
    tmp=line.split("|")
    if int(tmp[0]) in clusteringcoefficient23 and int(tmp[1]) in clusteringcoefficient23 and int(tmp[2]) in clusteringcoefficient23:
        a1=clusteringcoefficient23[int(tmp[0])]
        a2=clusteringcoefficient23[int(tmp[1])]
        a3=clusteringcoefficient23[int(tmp[2])]
        if a2!= 0:
            illegtripletlist.append((a1+a3)/a2)
    line=f.readline()
f.close()


f=open("clusteringcoefficientdifferenceanalysisilleg.txt",'w')
for item in illegtripletlist:
    f.write(str(item)+'\n')
f.close()

#在这里计算合法字典和非法字典中的分析,不使用accuracy以及F1 score的复杂指标了
#合法字典中的合法路径比例最多


