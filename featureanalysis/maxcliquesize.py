import networkx as nx
import time 

T1 = time.time()
fh = open("/home/jiang/data/routeleak/graphdata/collectgraph/20210601.as-rel2.txt", "rb")
G = nx.read_edgelist(fh,nodetype=int, data=(("weight", int),("source", str),), comments='#', delimiter="|")
fh.close()

cc={}
# cc=dict(nx.eccentricity(G))
cc=nx.node_clique_number(G)

f=open("maxcliquesize2021.txt",'w')
for item in cc:
    f.write(str(item)+"|"+str(cc[item])+'\n')
f.close()

T2 = time.time()
print("spend time:", T2-T1)
# 2021年，2022年的数据跑不出结果来，内存占用太多