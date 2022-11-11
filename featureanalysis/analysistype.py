from collections import defaultdict

asclassification={}
f=open("../../graphdata/collectgraph/asclassfication/20210401.as2types.txt")
line=f.readline()
while line:
    if '#' not in line:
        tmp=line.split("|")
        if tmp[2]=="Content\n":
            asclassification[int(tmp[0])]=0
        if tmp[2] == "Enterprise\n":
            asclassification[int(tmp[0])]=1
        if tmp[2] == "Transit/Access\n":
            asclassification[int(tmp[0])]=2
    line=f.readline()
f.close()
# print(len(asclassification))

#分析非法三元组的分布情况

illegitimateset=set()
f=open("illegitimate.txt")
line=f.readline()
while line:
    tmp=line.split("|")
    illegitimateset.add((int(tmp[0]),int(tmp[1]),int(tmp[2])))
    line=f.readline()
f.close()
illegtripledict = defaultdict(int)
for item in illegitimateset:
    if item[0] in asclassification and item[1] in asclassification and item[2] in asclassification:
        # print(asclassification[item[0]],asclassification[item[1]],asclassification[item[2]])
        illegtripledict[(asclassification[item[0]],asclassification[item[1]],asclassification[item[2]])]+=1
    else:
        print("无")

print("合法的路径有")
legitimateset=set()
f=open("legitimate.txt")
line=f.readline()
while line:
    tmp=line.split("|")
    legitimateset.add((int(tmp[0]),int(tmp[1]),int(tmp[2])))
    line=f.readline()
f.close()


legtripledict = defaultdict(int)
for item in legitimateset:
    if item[0] in asclassification and item[1] in asclassification and item[2] in asclassification:
        # print(asclassification[item[0]],asclassification[item[1]],asclassification[item[2]])
        legtripledict[(asclassification[item[0]],asclassification[item[1]],asclassification[item[2]])]+=1
    else:
        print("无")

print(legtripledict)
print("-----------------------------------")
print(illegtripledict)

#3个位置，每个位置上可以是0,1,2三种情况, 27种情况
# defaultdict(<class 'int'>, {(2, 2, 2): 869, (2, 2, 1): 75, (0, 2, 2): 16, (2, 2, 0): 50, (2, 0, 2): 15, (0, 2, 1): 5, (2, 1, 2): 8, (2, 0, 0): 9, (0, 0, 2): 2, (1, 2, 2): 8, (2, 0, 1): 4, (2, 1, 1): 2, (0, 2, 0): 3, (2, 1, 0): 1, (1, 2, 1): 1})
# -----------------------------------
# defaultdict(<class 'int'>, {(2, 2, 2): 205, (2, 2, 0): 4, (2, 0, 0): 1, (2, 2, 1): 3, (0, 2, 2): 1, (2, 0, 2): 8, (2, 1, 2): 2})
