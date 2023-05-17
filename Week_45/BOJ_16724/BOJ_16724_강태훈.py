import sys
sys.setrecursionlimit(10**6)
input = lambda : sys.stdin.readline().rstrip()

# 방향에 따른 좌표 변화량 선언
dx = {i:j for i,j in zip("URDL", (0,1,0,-1))}
dy = {i:j for i,j in zip("URDL", (-1,0,1,0))}

def find(v, parent):
    """ v의 부모노드 리턴 """
    if parent[v]!=v:
        parent[v] = find(parent[v], parent)
    return parent[v]

def union(v1, v2, parent):
    """ 두 집합 병합 """
    p1 = find(v1, parent)
    p2 = find(v2, parent)
    if p1!=p2:
        parent[min(p1, p2)] = max(p1, p2)

def main(board, n, m):
    """ 집합 당 하나의 대표 선출 """
    parent = {(j,i):(j,i) for i in range(n) for j in range(m)}
    # Vertex : coordinate, Link : coordinate <-> movable coordinate
    for y in range(n):
        for x in range(m):
            t = board[y][x]
            # 연결된 두 좌표 병합
            union((x,y), (x+dx[t], y+dy[t]), parent)
    # 사이클 개수만큼 대표 선출
    return len(set([find((x,y), parent) for x in range(m) for y in range(n)]))

if __name__ == "__main__":
    n, m = map(int, input().split())
    board = [input() for _ in range(n)]
    print(main(board, n, m))