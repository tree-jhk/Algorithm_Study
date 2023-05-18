N, M = map(int, input().split())

d = {"R":0, "L":1, "D":2, "U":3}
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def dfs(i, j, num):
    global answer
    if visited[i][j]:
        if visited[i][j] == num:
            answer += 1
        return
    visited[i][j] = num
    nx = i + dx[d[board[i][j]]]
    ny = j + dy[d[board[i][j]]]
    dfs(nx, ny, num)

board = []
for _ in range(N):
    board.append(list(input()))

answer = 0
num = 1
visited = [[0] * M for _ in range(N)]
for i in range(N):
    for j in range(M):
        if not visited[i][j]:
            dfs(i, j, num)
            num += 1
print(answer)