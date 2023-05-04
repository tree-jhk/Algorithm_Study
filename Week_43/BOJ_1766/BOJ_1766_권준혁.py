from collections import defaultdict
from heapq import *
        

def check_zero_indegree(indegree:list, hq:list):
    for i in range(1, n + 1):
        if indegree[i] == 0:
            heappush(hq, i)
    return hq

def update(hq:list, indegree:list, dag:dict, answer:list):
    node = heappop(hq)
    answer.append(node)
    for nxt in dag[node]:
        indegree[nxt] -= 1
        if indegree[nxt] == 0:
            heappush(hq, nxt)
    return hq, indegree, dag, answer

if __name__ == '__main__':
    n, m = map(int, input().split())
    dag = defaultdict(list)
    answer = []
    indegree = [0] * (n + 1) # 0번 노드는 padding
    hq = []
    for _ in range(m):
        r = list(map(int, input().split()))
        dag[r[0]].append(r[1])
        indegree[r[1]] += 1
    indegree = check_zero_indegree(indegree, hq)
    while(hq):
        hq, indegree, dag, answer = update(hq, indegree, dag, answer)
    print(*answer)