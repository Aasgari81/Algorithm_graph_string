import sys

def negative_cycle(adj, cost):
    #write your code here
    dist=[float('inf')]*len(adj)
    dist[0] = 0
    for i in range(len(adj)):
        for u in range(len(adj)):
            for v in adj[u]:
                v_index = adj[u].index(v)
                if dist[v] > dist[u] + cost[u][v_index]:
                    dist[v] = dist[u] + cost[u][v_index]
                    if i == len(adj) - 1:
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
    print(negative_cycle(adj, cost))