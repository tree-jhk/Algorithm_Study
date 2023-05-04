import sys
from heapq import heappush, heappop
input = sys.stdin.readline


def main(graph, in_degree, n, m):
    # 진입차수 0인 노드 heapq에 미리 저장. 저장된 순서는 노드번호 순으로 정렬된 형태 -> 쉬운문제부터 탐색, heapify 안해도 됨
    hq = [i for i in range(n) if in_degree[i]==0]
    answer = []
    while hq:
        # 진입차수 0이면 정답에 넣음
        c = heappop(hq)
        answer.append(c+1)
        for n in graph[c]:
            # 선택된 노드와 연결된 노드들 제거
            in_degree[n] -= 1
            if in_degree[n]==0:
                # 진입차수 0인 노드는 hq에 추가
                heappush(hq, n)
    print(*answer)
    return

if __name__ == "__main__":
    n, m = map(int, input().split())
    # 인접리스트 방식 graph
    graph = [[] for _ in range(n)]
    # 진입차수
    in_degree = [0 for _ in range(n)]
    # p노드에서 c노드로 가는 유향그래프
    for _ in range(m):
        p, c = map(lambda x:int(x)-1, input().split())
        graph[p].append(c)
        in_degree[c] += 1
    main(graph, in_degree, n, m)