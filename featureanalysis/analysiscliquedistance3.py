#统计不同的三元组的分布情况,up down flat三种状态，2段，9种状态
#其中，认为平，有一个阈值，相差不多即可认为平
#先分析合法的

#可以对程序做一个调参的改进，选择合适阈值使得，分类尽可能准确率高，通过变化参数，分别算出不同阈值下，准确率最好的一个阈值
from collections import defaultdict
# from operator import le

legitimate=[]
f=open("legitimatecliquedistance.txt")
line=f.readline()
while line:
    if 'unknown' not in line:
        tmp=line.split("|")
        a1=eval(tmp[0])
        a2=eval(tmp[1])
        a3=eval(tmp[2])
        legitimate.append((a1+a3)/a2)
    line=f.readline()

# print("合法的三元组的分布是")
# print(legitimate)
f.close()

f1=open("chalegicliquedistance3.txt",'w')
for item in legitimate:
    f1.write(str(item)+'\n')
f1.close()

illegitimate=[]
f=open("illegitimatecliquedistance.txt")
line=f.readline()
while line:
    if 'unknown' not in line:
        tmp=line.split("|")
        a1=eval(tmp[0])
        a2=eval(tmp[1])
        a3=eval(tmp[2])
        illegitimate.append((a1+a3)/a2)
    line=f.readline()

 
# print("不合法的三元组的分布是")
# print(illegitimate)
# f.close()

f1=open("chaleakcliquedistance3.txt",'w')
for item in illegitimate:
    f1.write(str(item)+'\n')
f1.close()