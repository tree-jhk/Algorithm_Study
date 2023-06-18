import sys
import math
input = sys.stdin.readline

def union(x, y):
    x = find(x)
    y = find(y)
    if x > y:
        parent[x] = y
    else:
        parent[y] = x

def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]

def MST():
    answer = 0
    for c, x, y in graph:
        if find(x) != find(y):
            union(x, y)
            answer += c
    return answer

if __name__ == "__main__":
    n = int(input())
    points = []
    for _ in range(n):
        x, y = map(float, input().split())
        points.append([x, y])
    
    graph = []
    for i in range(n - 1):
        for j in range(i + 1, n):
            xdiff = abs(points[i][0] - points[j][0])
            ydiff = abs(points[i][1] - points[j][1])
            dist = math.sqrt(xdiff ** 2 + ydiff ** 2)
            graph.append((dist, i, j))
    graph.sort()
    parent = [i for i in range(n + 1)]
    answer = MST()
    print(round(answer, 2))