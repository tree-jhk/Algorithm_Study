import heapq
import sys
input = sys.stdin.readline

def dijkstra(s, graph):
    dist = [float("inf") for _ in range(N)]
    dist[s] = 0
    q = []
    heapq.heappush(q, (s, dist[s]))
    while q:
        cur, d = heapq.heappop(q)
        if dist[cur] < d:
            continue
        for next, cost in graph[cur]:
            ndist = cost + d
            if ndist < dist[next]:
                dist[next] = ndist
                heapq.heappush(q, (next, dist[next]))
    
    return dist

if __name__ == "__main__":
    N, M, X = map(int, input().split())

    graph = [[] for _ in range(N)]
    revgraph = [[] for _ in range(N)]
    
    for _ in range(M):
        A, B, C = map(int, input().split())
        graph[A - 1].append([B - 1, C])
        revgraph[B - 1].append([A - 1, C])
    
    answer = 0
    toX = dijkstra(X - 1, graph)
    fromX = dijkstra(X - 1, revgraph)
    for i in range(N):
        answer = max(answer, toX[i] + fromX[i])
    print(answer)