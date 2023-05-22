from sys import stdin
from heapq import heappop, heappush
input = lambda : map(int, stdin.readline().split())

def dijkstra(graph, n, x):
    hq = [(0, x)]
    dist = [float("inf")]*(n+1)
    dist[x]=0
    while hq:
        cnt, node = heappop(hq)
        if cnt>dist[node]:
            continue
        for w, nnode in graph[node]:
            cost = w+cnt
            if cost<dist[nnode]:
                dist[nnode] = cost
                heappush(hq, (cost, nnode))
    return dist[1:]

def solve(n, x, go, back):
    answer = 0
    for i, j in zip(dijkstra(go, n, x), dijkstra(back, n, x)):
        answer = max(i+j, answer)
    print(answer)

if __name__ == "__main__":
    n, m, x = input()
    go = {i:[] for i in range(1, n+1)}
    back = {i:[] for i in range(1, n+1)}
    for _ in range(m):
        s, e, w = input()
        go[s].append((w, e))
        back[e].append((w, s))
    solve(n, x, go, back)