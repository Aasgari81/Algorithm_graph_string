import sys
import copy
from collections import deque



def shortest_paths(adj, cost, s, distance, reachable, shortest) :
    isNG, reachablefromNG, distance, prevs = negativeCycle(adj, cost, s)
    if isNG == 1 :
        negativecycle = findnegativecycle(prevs, reachablefromNG)
        reachablesfromNG = reachables(adj, negativecycle)
        for i in range(len(adj)) :
            if i in reachablesfromNG:
                shortest[i] = 0
            
    
    elif isNG == 0 :
        for i in range(len(reachable)) :
            shortest[i] = 1

    
    for i in range (len(distance)) :
        if distance[i] != float('inf'):
            reachable[i] = 1
    return reachable, shortest, distance
    


def negativeCycle(adj, cost,s):
    vertexnumber = len(adj)
    edges = []
    for i in range(vertexnumber) :
        adjs = adj[i]
        for m in range(len(adjs)) :
            edges.append((i, adjs[m], cost[i][m]))
    prev = [None] * vertexnumber
    dist = [float('inf')] * vertexnumber
    
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
            return 1, i, dist, prev
    return 0, 5, dist, prev





            

def findnegativecycle(prev, reachableFNG) :
    m = reachableFNG
    reachables = []
    reachables.append(m)
    cycle = []
    for i in range(len(prev)) :
        m = prev[m]
        if m not in reachables :
            reachables.append(m)
        elif m in reachables and m not in cycle :
            cycle.append(m)
        elif m in cycle :
            break
    return cycle
        



def reachables (adj, negativesycle) :
    result = set()
    for i in negativesycle :
        result.add(i)
    bfsresult = bfs(adj, negativesycle[0], negativesycle[1])
    for i in bfsresult :
        result.add(i)
    return result




def bfs(adj, start, end):
    reachables = []
    q = deque()
    check = {}
    dist = [2147483647] * len(adj)

    for i in range(len(adj)):
        dist[i] = 2147483647

    for j in range(len(adj)):
        check[j] = False

    if start == end:
        return 0

    dist[start] = 0
    q.append(start)
    while len(q) > 0:
        k = q.popleft()
        check[k] = True
        for o in adj[k]:
            if not check[o]:
                q.append(o)
                dist[o] = dist[k] + 1
                check[o] = True
                reachables.append(o)

    return reachables





if __name__ == '__main__':
    n, m = map(int, input().split())
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for i in range(m):
        x, y, w = map(int, input().split())
        adj[x - 1].append(y - 1)
        cost[x - 1].append(w)
    s = int(input()) - 1
    distance = [0] * n
    reachable = [0] * n
    shortest = [1] * n
    reachable,shortest,distance = shortest_paths(adj, cost, s, distance, reachable, shortest)
    for i in range(n):
        if reachable[i] == 0:
            print('*')
        elif shortest[i] == 0:
            print('-')
        else:
            print(distance[i])