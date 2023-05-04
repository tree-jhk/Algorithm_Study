import sys
import heapq

n, m = map(int, sys.stdin.readline().rstrip().split())
nodes = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    # 간선은 방향성이 없다.
    nodes[a].append([b, c])
    nodes[b].append([a, c])
INF = sys.maxsize

"""
합리적인 이동경로:
- 한 정점 S에서 다른 한 정점 T로 이동하려 한다. 
- 이동할 때 T에 가까워지며 이동하는 경우
    - dist(u, v) = 정점 u와 v의 사이의 거리
    - 정점 S에서 X로 이동할 때,
        - dist(S, T) > dist(X, T)
        - 즉 다른 정점에서 출발하는 것이 더 짧은 경로
- 현재 노드까지 최단 경로의 길이 > 다음 노드까지 최단 경로의 길이라면 
- 다음 노드와 현재 노드 사이에 "합리적인 이동경로"가 존재한다는 뜻이 된다.
"""

# 다익스트라 알고리즘: 특정 정점에서 다른 정점으로 가는 최단 경로 알고리즘
# 다익스트라는 현재까지 알고 있던 최단 경로를 활용해서 계속해서 최단 경로를 갱신하는 알고리즘
# 역방향으로 다익스트라를 진행해야함 == 도착 지점 T = 2에서 부터 최단 경로 진행
# start(T=2) 지점에서부터 시작
def Dijsktra(start):
    # distances[i]: start -> i로 가는 최단 거리
    # 일단 모두 INF로 초기화
    distances = [INF for _ in range(n+1)]
    distances[start] = 0

    hq = []
    heapq.heappush(hq, [0, start])

    while hq:
        # dist(start, cur_node) = cur_cost
        cur_cost, cur_node = heapq.heappop(hq)

        # start -> cur_node로 가는 최단 거리 < 현재까지 알고 있던 최단 경로
        # False 조건: INF보다 작거나, 새로운 최단 경로 갱신될 때
        if distances[cur_node] < cur_cost:
            continue
        
        # cur_node와 인접한 next_node들
        for next_node, next_cost in nodes[cur_node]:
            # start -> next_node 거리 > start -> cur_node -> next_node 거리
            # == 즉 next_node까지 갈 때, 기존의 최단경로보다 cur_node를 거칠 때가 더 짧은 경로인 경우
            if distances[next_node] > cur_cost + next_cost:
                distances[next_node] = cur_cost + next_cost
                heapq.heappush(hq, [cur_cost + next_cost, next_node])
    return distances

# distances: 2 -> 정점들까지 가는 최단경로
distances = Dijsktra(2)

def rational_path(cur_node):
    if dp[cur_node] == 0:
        for next_node, next_cost in nodes[cur_node]:
            if distances[cur_node] > distances[next_node]:
                # cur_node보다 next_node 사용이 T에 도달하는 더 합리적인 이동 경로.
                dp[cur_node] += rational_path(next_node)
        return dp[cur_node]
    else:
        return dp[cur_node]


dp = [0 for _ in range(n+1)]
dp[2] = 1
# T -> T일 때 1로 취급
print(rational_path(1))