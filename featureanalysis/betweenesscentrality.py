import networkx as nx
import time 

T1 = time.time()
# fh = open("/home/jiang/data/routeleak/graphdata/collectgraph/20230101.as-rel2.txt", "rb")
# fh = open("/home/jiang/data/routeleak/graphdata/collectgraph/20220601.as-rel2.txt", "rb")
fh = open("/home/jiang/data/routeleak/graphdata/collectgraph/20210601.as-rel2.txt", "rb")

G = nx.read_edgelist(fh,nodetype=int, data=(("weight", int),("source", str),), comments='#', delimiter="|")
fh.close()

bc={}
bc=nx.betweenness_centrality(G)


# f=open("betweenesscentrality.txt",'w')
# f=open("betweenesscentrality2022.txt",'w')
f=open("betweenesscentrality2021.txt",'w')
for item in bc:
    f.write(str(item)+"|"+str(bc[item])+'\n')
f.close()

T2 = time.time()
print("spend time:", T2-T1)
