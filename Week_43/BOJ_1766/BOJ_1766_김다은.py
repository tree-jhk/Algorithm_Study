from queue import PriorityQueue

if __name__ == "__main__":
    answer = []
    N, M = map(int, input().split())
    graph = [[] for _ in range(N + 1)]
    indegree = [0] * (N + 1)

    for i in range(M):
        A, B = map(int, input().split())
        graph[A].append(B)  
        indegree[B] += 1

    q = PriorityQueue()
    for i in range(1, N + 1):
        if indegree[i] == 0:
            q.put(i)
    while q.qsize():
        tmp = q.get()
        answer.append(tmp)
        for i in graph[tmp]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.put(i)
    print(" ".join(map(str, answer)))