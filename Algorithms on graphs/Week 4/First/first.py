# import the heapq module for implementing a priority queue
import heapq

def main():
    # read the number of nodes and edges
    n, m = map(int, input().split())
    # initialize the adjacency list and the cost list
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    # read the edges and their weights
    for _ in range(m):
        x, y, w = map(int, input().split())
        # subtract 1 from x and y to make them zero-based indices
        x -= 1
        y -= 1
        adj[x].append(y)
        cost[x].append(w)
    # read the source and target nodes
    s, t = map(int, input().split())
    # subtract 1 from s and t to make them zero-based indices
    s -= 1
    t -= 1
    # print the result of the shortest path algorithm
    print(distance(adj, cost, s, t))

def distance(adj, cost, s, t):
    # get the number of vertices
    vertex_numbers = len(adj)
    # initialize the previous array
    prev = [None] * vertex_numbers
    # initialize the priority queue as a list of tuples (cost, vertex)
    pq = []
    # initialize the distance array with infinity values
    dist = [float('inf')] * vertex_numbers
    # set the distance of the source node to zero
    dist[s] = 0
    # set the previous of the source node to itself
    prev[s] = s
    # push the source node to the priority queue with zero cost
    heapq.heappush(pq, (0, s))
    # push all other nodes to the priority queue with infinity cost
    for i in range(vertex_numbers):
        if i != s:
            heapq.heappush(pq, (float('inf'), i))
    # loop until the priority queue is empty
    while pq:
        # pop the node with the lowest cost from the priority queue
        u_cost, u = heapq.heappop(pq)
        # loop through all the neighbors of u
        for i in range(len(adj[u])):
            v = adj[u][i]
            # if the distance of v can be improved by going through u
            if dist[v] > dist[u] + cost[u][i]:
                # update the distance of v
                dist[v] = dist[u] + cost[u][i]
                # update the previous of v
                prev[v] = u
                # update the cost of v in the priority queue by pushing a new tuple with lower cost (this will not remove the old tuple)
                heapq.heappush(pq, (dist[v], v))
    
    # if the target node is unreachable, return -1
    if dist[t] == float('inf'):
        return -1
    
    # otherwise, return the distance of t
    return dist[t]

# call the main function
if __name__ == '__main__':
    main()