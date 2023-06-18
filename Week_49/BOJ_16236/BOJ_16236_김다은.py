from collections import deque

def bfs():
    visited = [[-1] * n for _ in range(n)]
    q = deque([[sx, sy, 0]])
    result = []
    visited[sx][sy] = 0
    while q:
        cx, cy, dist = q.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if nx >= n or nx < 0 or ny >= n or ny < 0:
                continue
            if visited[nx][ny] == -1:
                # 이 칸으로 이동할 수 있는지
                if board[nx][ny] <= size:
                    visited[nx][ny] = dist + 1
                    q.append([nx, ny, dist + 1])
                    # 이 칸의 물고기를 잡아먹을 수 있는지
                    if 0 < board[nx][ny] < size:
                        result.append([dist + 1, nx, ny])
    # 거리가 가까운 물고기가 많다면, 가장 위에 있는 물고기, 
    # 그러한 물고기가 여러마리라면, 가장 왼쪽에 있는 물고기를 먹는다.
    return sorted(result)

def sharkPosition():
    for i in range(n):
        for j in range(n):
            if board[i][j] == 9:
                return [i, j]

if __name__ == "__main__":
    n = int(input())
    board = []
    for _ in range(n):
        board.append(list(map(int, input().split())))
    size = 2    # 아기 상어 크기
    sx, sy = sharkPosition()
    board[sx][sy] = 0
    answer = 0
    eatCnt = 0
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    while True:
        result = bfs()
        if len(result) == 0:
            break
        dist, fx, fy = result[0]
        # 잡아먹는다.
        board[fx][fy] = 0
        eatCnt += 1
        # 자신의 크기와 같은 수의 물고기를 먹으면 크기 1 증가
        if eatCnt == size:
            size += 1
            eatCnt = 0
        sx, sy = fx, fy
        answer += dist
print(answer)