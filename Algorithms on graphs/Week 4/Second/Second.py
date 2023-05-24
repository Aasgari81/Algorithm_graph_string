# import the sys module for reading input
import sys
import copy
def negativeCycle(adj, cost):
    vertexnumber = len(adj)
    edges = []
    for i in range(vertexnumber) :
        adjs = adj[i]
        for m in range(len(adjs)) :
            edges.append((i, adjs[m], cost[i][m]))
    prev = [None] * vertexnumber
    dist = [float('inf')] * vertexnumber
    s = 0
    dist[s] = 0
    prev[s] = s
    for i in range(vertexnumber - 1) :
        for i in edges :
            start, end, Mcost = i
            if dist[end] > dist[start] + Mcost :
                dist[end] = dist[start] + Mcost
                prev[end] = start
    forcheck = copy.deepcopy(dist)
    for i in edges :
            start, end, Mcost = i
            if dist[end] > dist[start] + Mcost :
                dist[end] = dist[start] + Mcost
                prev[end] = start
    for i in range(len(forcheck)) :
        if dist[i] != forcheck[i] :
            return 1
    return 0




if __name__ == "__main__" :

    # read the number of nodes and edges
    n, m = map(int, sys.stdin.readline().split())

    # initialize the adjacency list and the cost list
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]

    # read the edges and their weights
    for _ in range(m):
        x, y, w = map(int, sys.stdin.readline().split())
        # subtract 1 from x and y to make them zero-based indices
        adj[x - 1].append(y - 1)
        cost[x - 1].append(w)
    
    # print the result of the negative cycle detection
    print(negativeCycle(adj, cost))