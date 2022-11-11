import copy
def removeanomaly(hops):
    anomaly=[0,23456,65535]
    tmphops=copy.copy(hops)
    for item in hops:
        if eval(item) in anomaly or (eval(item)<64511 and eval(item)>64496) or (eval(item)<64512 and eval(item)>65534):
            tmphops.remove(item)
    print(hops)
    print(tmphops)
    return tmphops


hops=['1','2','3','4','5','0']
print(removeanomaly(hops))
