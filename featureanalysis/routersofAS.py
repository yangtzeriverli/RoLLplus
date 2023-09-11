f=open("midar-iff.nodes.as.2021")

ASrouter={}
line=f.readline()
while line:
    tmp=line.split(" ")   #2021
    # tmp=line.split("\t")  2022
    ASrouter.setdefault(tmp[2],set()).add(tmp[1])
    line=f.readline()

f.close()


f=open("routersofAS2021.txt",'w')
for item in ASrouter:
    f.write(str(item)+"|"+str(len(ASrouter[item]))+"\n")

f.close()