import sys
import math

def minimum_distance(x, y):
    result = 0.
    result_edges = []
    #disjoint set
    djs = {}
    verticies = {}
    edges = {}
    n = len(x)
    for i in range(n) :
        verticies[i] = (x[i], y[i])
    for i in range(n) :
        for j in range(n) :
           edges[(i,j)] = None
    
    for i in range(n) :
        for j in range(n) :
            if edges[(i, j)] == None :
                dist = math.sqrt((x[i]-x[j])**2 + (y[i] - y[j])**2)
                edges[(i,j)] = dist
                edges[(j, i)] = dist

    for i in range(n) :
        djs[i] = i
    edges = dict(sorted(edges.items(), key=lambda item: item[1]))

    for e in edges.keys() :
        u,v = e[0], e[1]
        if find(djs, u) != find(djs, v) :
            result_edges.append(e)
            djs = union(djs, v, u)
    for edge in result_edges :
        result += edges[edge]
    return result



#returns the root of a disjoint set
def find(dsj, vertex) : 
    m = vertex
    while dsj[m] != m:
        m = dsj[m]
    return m


def union (dsj, v1, v2) :
    dsj[find(dsj, v1)] = find(dsj, v2)
    return dsj



if __name__ == '__main__':
    n = int(input())
    x = [0]*n
    y = [0]*n
    for i in range(n):
        x[i], y[i] = map(int, input().split())
    print("{:.9f}".format(minimum_distance(x, y)))

