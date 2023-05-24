from collections import deque

def reach(adj, start, end):
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
