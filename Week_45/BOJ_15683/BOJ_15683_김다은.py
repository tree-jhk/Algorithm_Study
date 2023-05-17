from copy import deepcopy

# CCTV 종류별로 볼 수 있는 방향
# 0:상, 1:우, 3:하, 4:좌
type = [
    [],
    [[0], [1], [2], [3]],
    [[0, 2], [1, 3]],
    [[0, 1], [1, 2], [2, 3], [0, 3]],
    [[0, 1, 2], [1, 2, 3], [0, 2, 3], [0, 1, 3]],
    [[0, 1, 2, 3]]
    ]

# 위, 오, 아, 왼
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# cctv가 볼 수 있는 방향 7로 채워줌
def watch(temp, c, x, y):
    for i in c:
        nx = x
        ny = y
        while True:
            nx += dx[i]
            ny += dy[i]
            if nx >= N or nx < 0 or ny >= M or ny < 0:  # 범위 벗어남
                break
            if temp[nx][ny] == 6:   # 벽
                break
            else:
                temp[nx][ny] = 7

def solution(depth, arr):
    global answer
    if depth == num:
        # 사각지대 개수 세주기(0이 사각지대)
        cnt = 0
        for i in range(N):
            for j in range(M):
                if arr[i][j] == 0:
                    cnt += 1
        answer = min(answer, cnt)
        return
    temp = deepcopy(arr)
    c, x, y = cctv[depth]   # cctv 번호, 좌표
    for i in type[c]:   # 이 cctv 번호가 볼 수 있는 방향
        watch(temp, i, x, y)
        solution(depth + 1, temp)
        temp = deepcopy(arr)

N, M = map(int, input().split())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

num = 0 # cctv 개수
cctv = []
for i in range(N):
    for j in range(M):
        if 1 <= board[i][j] <= 5:
            num += 1
            cctv.append([board[i][j], i, j])
answer = 1e9
solution(0, board)
print(answer)