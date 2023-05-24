import sys
import math

def clustering(x, y, k, n):
    verticies = {}
    edges_weight = {}
    #disjoint set
    djs = []
    for i in range(n) :
        verticies[i] = (x[i], y[i])
    for i in range(n) :
        for j in range(n) :
           edges_weight[(i,j)] = None
    for i in range(n) :
        for j in range(n) :
            if edges_weight[(i, j)] == None :
                dist = math.sqrt((x[i]-x[j])**2 + (y[i] - y[j])**2)
                edges_weight[(i,j)] = dist
                edges_weight[(j, i)] = dist
    edges_weight = dict(sorted(edges_weight.items(), key=lambda item: item[1]))
    for i in range(n) :
        djs.append([i])
    

    for e in edges_weight.keys() :
        if len(djs) <= k :
            break
        u,v = e[0], e[1]
        m = 0 
        q = 0
        for i in range(len(djs)) :
            if v in djs[i] :
                m = i
                break
        for i in range(len(djs)) :
            if u in djs[i] :
                q = i
                break
        if u not in djs[m] :
            for s in djs[q] :
                djs[m].append(s)
            djs.remove(djs[q])
    
    #In this part the data sets are clustered 
    result = float('inf')
    for i in djs :
        for j in djs :
            if i == j :
                continue
            for e1 in i :
                for e2 in j :
                    if edges_weight[e1, e2] < result :
                        result = edges_weight[e1, e2]
    return result








if __name__ == '__main__':
    n = int(input())
    x = [0] * n
    y = [0] * n
    for i in range(n):
        x[i], y[i] = map(int, input().split())
    k = int(input())
    print("{:.12f}".format(clustering(x, y, k, n)))
