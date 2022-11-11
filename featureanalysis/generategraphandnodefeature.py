#图的生成没有问题了，下面就是生成点的特征，最终的输出是一个字典，键是AS，值是这个AS的特征
import json
from collections import deque
import time

time_start=time.time()

def find1hopneighbor(tmp_as):
    tmp_neighbor=set()
    for item in aslinkdict[tmp_as]:
        tmp_neighbor.add(item)
    return tmp_neighbor

def isNotVisited(x,path):
    size = len(path)
    for i in range(size):
        if (path[i] == x):
            return 0
    return 1

#输入源item,目的地 cliqueitem,返回从源到目的地的BFS的距离
def findpathlen(src,dst):
    count=0
    q=deque()
    path=[]
    path.append(src)
    q.append(path.copy())

    while q:
        count+=1
        path=q.popleft()
        last=path[len(path)-1]
        if last == dst:
            break
        candidate = find1hopneighbor(last)
        for candi in candidate:
            #这个检测是为了防止环路，如果邻居已经在路径上就不加了
            if (isNotVisited(candi, path)):
                newpath = path.copy()
                newpath.append(candi)
                q.append(newpath)
    
    if len(q)==0:
        #src和dst之间不可达,q空退出循环
        return 1000
    else:
        #break退出循环
        return len(path)


def bfs(src):
    visited = []
    queue = []
    visited.append(src)
    queue.append(src)
    
    while queue:
        s = queue.pop(0)
        #弹出列表的第一个item
        #自己到自己的路径长度是1

        # print (s, end = " ") 

        for neighbour in aslinkdict[s]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
                asasbfs[(src,neighbour)]=asasbfs[(src,s)]+1



f=open("20220801.as-rel2.txt")
f1=open("../graph/new20220801.as-rel2.txt",'w')
f2=open("../nodefeature/20220801node.txt",'w')
asset=set()
ixpaslist=[]
cliqueaslist=[]
asclassification={}
asdegree={}
aslinkdict={}
#不记录商业关系，邻接链表，只记录邻居点的集合
asasbfs={}
#键是元组(srcAS,dstAS),值是距离
asdistanceavg={}
asfeature={}
line=f.readline()
while line:
    if "source" not in line:
        if "clique" not in line:
            if "IXP" not in line:
                f1.write(line)
                #f1文件中是去掉头部的as-rel文件,下面是对实际的link进行处理
                tmp=line.split("|")
                asset.add(int(tmp[0]))
                asset.add(int(tmp[1]))
                aslinkdict.setdefault(int(tmp[0]),set()).add(int(tmp[1]))
                aslinkdict.setdefault(int(tmp[1]),set()).add(int(tmp[0]))
            else:
                tmp=line.split(": ")
                tmplist=tmp[1].split(" ")
                for item in tmplist:
                    ixpaslist.append(int(item))

        else:
            tmp=line.split(": ")
            tmplist=tmp[1].split(" ")
            for item in tmplist:
                cliqueaslist.append(int(item))


    line=f.readline()

f.close()
f1.close()


# print(cliqueaslist)
# print(ixpaslist)
# print(len(asset))

for item in asset:
    asdegree[item]=0

f1=open("../graph/new20220801.as-rel2.txt")
line=f1.readline()
while line:
    tmp=line.split("|")
    asdegree[int(tmp[0])]+=1
    asdegree[int(tmp[1])]+=1
    line=f1.readline()
f1.close()

# for item in asset:
#     #计算每个点到clique层AS的最短路径（作为距离），使用最短路径能减少选择valley路径的可能性,毕竟是估算去上面的距离，valley的路径会向下走一段，加大这个距离
#     sumdistance=0
#     for cliqueitem in cliqueaslist:
#         #计算sumdistance，计算每个源点item到clique AS的最短距离
#         sumdistance+=findpathlen(item,cliqueitem)
#     asdistanceavg[item]=sumdistance/len(cliqueaslist)
#     print(asdistanceavg[item])
for cliqueitem in cliqueaslist:
    asasbfs[(cliqueitem,cliqueitem)]=1
    bfs(cliqueitem)
    #得到从clique as到其他AS的BFS的距离

for item in asset:
    sumdistance=0
    for cliqueitem in cliqueaslist:
        if (cliqueitem,item) in asasbfs:
            sumdistance+=asasbfs[(cliqueitem,item)]
        else:
            sumdistance+=1000
            #不可达
    asdistanceavg[item]=sumdistance/len(cliqueaslist)
    # print(asdistanceavg[item])
    # 大概半个小时

        



#20210401之后没有数据了，只能一直用20210401的数据
f3=open("./asclassfication/20210401.as2types.txt")
line=f3.readline()
while line:
    if '#' not in line:
        tmp=line.split("|")
        if tmp[2]=="Content\n":
            asclassification[int(tmp[0])]=0
        if tmp[2] == "Enterprise\n":
            asclassification[int(tmp[0])]=1
        if tmp[2] == "Transit/Access\n":
            asclassification[int(tmp[0])]=2
    line=f3.readline()
f3.close()

org={}
astoorg={}
f4=open("./asorg/20220701.as-org2info.txt")
line=f4.readline()
while line:
    if "# format" not in line:
        tmp=line.split("|")
        if len(tmp)==5:
            #第一种数据 org_id|changed|org_name|country|source
            org[tmp[0]]=(tmp[2],tmp[3])
            # org_id:(org_name,country)
        if len(tmp)==6:
            #第二种数据  # format:aut|changed|aut_name|org_id|opaque_id|source
            astoorg[int(tmp[0])]=(tmp[2],tmp[3])
            # ASN:(aut_name,org_id)
    line=f4.readline()
f4.close()

#键是AS,值是元祖(组织ID，组织名称，AS名字，所属国家)
asorgall={}
for item in astoorg:
    asorgall[item]=(astoorg[item][1],org[astoorg[item][1]][0],astoorg[item][0],org[astoorg[item][1]][1])
# print(asorgall[1])

f5=open("./as2prefix/routeviews-rv2-20220801-0400.pfx2as")
import re
asprefixdict={}
line=f5.readline()
while line:
    tmp=line.split()
    # print(tmp[2])
    tmp2list=re.split(r'[_,]',tmp[2])
    for item in tmp2list:
        asprefixdict.setdefault(int(item),[]).append(eval(tmp[1]))
    # if eval(tmp[1]) > 24:
    #     print(line)
    #经过这个统计，竟然真的有超过24的长度的，甚至还有32的，那么就只能以32长度为一个单位进行统计

    line=f5.readline()
f5.close()

# print(asprefixlist)
asprefixspacedict={}
for key in asprefixdict:
    asprefixspacedict[key]=0
    for value in asprefixdict[key]:
        asprefixspacedict[key]+=pow(2,(32-value))
#每个AS有多少个地址
# print(asprefixspacedict)

#IXP数据
asixp={}

with open("./ixp/ix-asns_202207.json",'r') as load_f:
    load_dict = json.load(load_f)
    # print(load_dict)
    
# load_dict['smallberg'] = [8200,{1:[['Python',81],['shirt',300]]}]
# print(len(load_dict))
for item in load_dict:
    asixp.setdefault(item['asn'],set()).add(item['ix_id'])
    

#点的transit degree
td={}
f6=open("./transitdegree/20220801.transitdegree.txt")
line=f6.readline()
while line:
    tmp=line.split("|")
    td[int(tmp[0])]=int(tmp[1])
    line=f6.readline()
f6.close()

#输出了
#往下面加字段
for ASitem in asset:
    f2.write(str(ASitem)+"|")
    if ASitem in cliqueaslist:
        f2.write("1|")
    else:
        f2.write("0|")
    if ASitem in ixpaslist:
        f2.write("1|")
    else:
        f2.write("0|")
    if ASitem in asclassification:
        f2.write(str(asclassification[ASitem])+"|")
    else:
        f2.write(str('-1|'))
    if ASitem in asorgall:
        f2.write(asorgall[ASitem][0]+"|"+asorgall[ASitem][1]+"|"+asorgall[ASitem][2]+"|"+asorgall[ASitem][3]+"|")
    else:
        f2.write("-1|-1|-1|-1|")
    if ASitem in asprefixspacedict:
        f2.write(str(asprefixspacedict[ASitem])+"|")
    else:
        f2.write(str('-1|'))
    if ASitem in asixp:
        #一个AS可能在多个IXP中，直接输出是大括号{}
        f2.write(str(asixp[ASitem])+"|")
        # f2.write()
    else:
        #不在ixp中
        f2.write(str('-1|'))
    if ASitem in asdegree:
        f2.write(str(asdegree[ASitem])+"|")
    else:
        f2.write(str('-1|'))
    if ASitem in asdistanceavg:
        f2.write(str(asdistanceavg[ASitem])+"|")
    else:
        f2.write(str('-1|'))
    if ASitem in td:
        f2.write(str(td[ASitem]))
    else:
        f2.write(str('-1'))
    

    f2.write("\n")

f2.close()

time_end=time.time()
print('time cost',time_end-time_start,'s')