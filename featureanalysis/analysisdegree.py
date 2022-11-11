#统计不同的三元组的分布情况,up down flat三种状态，2段，9种状态
#其中，认为平，有一个阈值，相差不多即可认为平
#先分析合法的

#可以对程序做一个调参的改进，选择合适阈值使得，分类尽可能准确率高，通过变化参数，分别算出不同阈值下，准确率最好的一个阈值
from collections import defaultdict
# from operator import le

flatthrehold=0
step=1
f3=open("degreeparameter.txt",'w')

#0.01的时候
# 最大和是: 1.5924625468164795
# 对应的阈值是: 0.2700000000000001----取这个的时候，相对能获得一个较好的结果，合法的三元组
#0.001
# 最大和是: 1.5924625468164795
# 对应的阈值是: 0.2640000000000002

#换成6月份的数据的话
# 最大和是: 1.599098798397864
# 对应的阈值是: 0.3200000000000001


maxsum=0
maxthrehold=0

while flatthrehold<=100:
    legtripledict = defaultdict(int)
    f=open("legitimatedegree2022.txt")
    line=f.readline()
    while line:
        if 'unknown' not in line:
            tmp=line.split("|")
            a1=eval(tmp[0])
            a2=eval(tmp[1])
            a3=eval(tmp[2])
            if a1-a2>flatthrehold:
                b1='down'        
            elif a2-a1>flatthrehold:
                b1='up'
            else:
                b1='flat'
            if a3-a2>flatthrehold:
                b2='up'        
            elif a2-a3>flatthrehold:
                b2='down'
            else:
                b2='flat'
            legtripledict[(b1,b2)]+=1
        line=f.readline()

    # print("合法的三元组的分布是")
    # print(legtripledict)
        


    f.close()

    #在分析不合法的
    illegtripledict = defaultdict(int)
    f=open("illegitimatedegree2022.txt")
    line=f.readline()
    while line:
        if 'unknown' not in line:
            tmp=line.split("|")
            a1=eval(tmp[0])
            a2=eval(tmp[1])
            a3=eval(tmp[2])
            if a1-a2>flatthrehold:
                b1='down'        
            elif a2-a1>flatthrehold:
                b1='up'
            else:
                b1='flat'
            if a3-a2>flatthrehold:
                b2='up'        
            elif a2-a3>flatthrehold:
                b2='down'
            else:
                b2='flat'
            illegtripledict[(b1,b2)]+=1
        line=f.readline()

    # print("不合法的三元组的分布是")
    # print(illegtripledict)
    f.close()

    #在这里计算合法字典和非法字典中的分析,不使用accuracy以及F1 score的复杂指标了
    #合法字典中的合法路径比例最多
    count1=0
    for item in legtripledict:
        if item == ('down','up'):
            count1+=legtripledict[item]
        if item == ('down','flat'):
            count1+=legtripledict[item]
        if item == ('flat','up'):
            count1+=legtripledict[item]
        if item == ('flat','flat'):
            count1+=legtripledict[item]
    sum1=0
    for item in legtripledict:
        sum1+=legtripledict[item]
    p1=(sum1-count1)/sum1
    #p1最大

    count2=0
    for item in illegtripledict:
        if item == ('down','up'):
            count2+=illegtripledict[item]
        if item == ('down','flat'):
            count2+=illegtripledict[item]
        if item == ('flat','up'):
            count2+=illegtripledict[item]
        if item == ('flat','flat'):
            count2+=illegtripledict[item]
    sum2=0
    for item in illegtripledict:
        sum2+=illegtripledict[item]
    p2=count2/sum2

    if p1+p2 > maxsum:
        maxsum=p1+p2
        maxthrehold=flatthrehold
    
    #非法字典中的非法路径比例最多
    f3.write(str(flatthrehold)+"|"+str(p1)+"|"+str(p2)+"\n")

    
    flatthrehold+=step

f3.close()
print("最大和是:",maxsum)
print("对应的阈值是:",maxthrehold)