import sys
from heapq import heappush, heappop
input = sys.stdin.readline

# 거리를 weight로 바꾸는 함수
get_distance = lambda v1, v2 : sum((d1-d2)**2 for d1, d2 in zip(v1, v2))**0.5


def main(stars, n):
    # 두 정점 간 거리를 weight로 하는 그래프 선언 / dense한 그래프이므로 프림알고리즘 선택
    graph = [[get_distance(stars[i], stars[j]) for j in range(n)] for i in range(n)]
    visited = [False for i in range(n)] # 방문처리 배열 선언
    hq = [(0, 0)]
    total_w = 0
    
    while hq: # 우선순위큐를 활용한 Prim 알고리즘 최적화
        dist, cnode = heappop(hq)
        if not visited[cnode]:
            total_w += dist
            visited[cnode] = True
            for nnode, weight in enumerate(graph[cnode]):
                if cnode != nnode and not visited[nnode]:
                    heappush(hq, (weight, nnode))
    return round(total_w, 2)

if __name__ == "__main__":
    n = int(input())
    stars = [list(map(float, input().split())) for _ in range(n)]
    print(main(stars, n))