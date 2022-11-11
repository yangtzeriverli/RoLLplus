from itertools import groupby
import pybgpstream
import copy

def removeanomaly(hops):
    anomaly=[0,23456,65535]
    tmphops=copy.copy(hops)
    for item in hops:
        if eval(item) in anomaly or (eval(item)<64511 and eval(item)>64496) or (eval(item)<64512 and eval(item)>65534):
            tmphops.remove(item)
    return tmphops
stream = pybgpstream.BGPStream(
    # accessing routeview-stream
    project="routeviews-stream",
    # filter to show only stream from amsix bmp stream
    filter="router amsix",
)


AStriplet=set()
f=open("AStriplet.txt",'w')
for item in AStriplet:
    f.write(item[0]+'|'+item[1]+"|"+item[2]+'\n')

for elem in stream:
    tmpstr=str(elem)
    tmp=tmpstr.split("|")
    if tmp[1] == "A":
        hops=  [k for k, g in groupby(tmp[11].split(" "))]
        hops=removeanomaly(hops)  
        if len(hops) > 2:
            for i in range(1,len(hops)-1):
                if (hops[i-1],hops[i],hops[i+1]) not in AStriplet:
                    AStriplet.add((hops[i-1],hops[i],hops[i+1]))
                else:
                    pass

f.close()