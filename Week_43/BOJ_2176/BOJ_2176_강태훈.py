import sys
from heapq import heappush, heappop
input = sys.stdin.readline

def main(graph, n, m):
    # i까지의 거리
    dist = [float("inf")]*n
    dp = [0]*n
    dist[1], dp[1] = 0, 1
    
    hq = [[0, 1]]

    while hq:
        c_cost, c_node = heappop(hq)
        # 비용이 이미 초과된 상태면 무시
        if dist[c_node] < c_cost:
            continue
        for w, n_node in graph[c_node]:
            # (a -> b -> t) < (a -> t)이면 합리적인 이동경로이다.
            n_cost = c_cost + w
            # 합리적인 이동경로면 확장
            if dist[n_node] > n_cost:
                dist[n_node] = n_cost
                heappush(hq, [n_cost, n_node])
            # 메모이제이션, 경우의 수가 더해지면 됨
            if c_cost > dist[n_node]:
                dp[c_node] += dp[n_node]
    return dp[0]

if __name__ == "__main__":
    n, m = map(int, input().split())
    graph = [[] for _ in range(n)]
    # 가중치를 가지는 인접리스트 그래프
    for _ in range(m):
        a, b, c = map(int, input().split())
        graph[a-1].append([c, b-1])
        graph[b-1].append([c, a-1])
    print(main(graph, n, m))