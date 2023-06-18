import sys
from heapq import heappush, heappop
input = sys.stdin.readline

dx = (0,-1,1,0)
dy = (-1,0,0,1)
def get_near(x, y, n): # 인접 좌표 리턴하는 유틸용 함수
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 0<=nx<n and 0<=ny<n:
            yield nx, ny

def choice(board, shark_loc, shark_size, n): # 잡아먹을 물고기 위치 탐색
    x, y = shark_loc
    hq = [(0,y,x)] # 우선순위큐 개념으로 거리, y, x 순으로 작은값 보장
    visited = [[False]*n for _ in range(n)]; visited[y][x] = True # 방문처리 배열 선언
    while hq:
        dist, cy, cx = heappop(hq)
        if 0<board[cy][cx]<shark_size: # 가장 먼저 찾은 잡아먹을 수 있는 물고기 좌표 리턴
            return (cx, cy), dist
        for nx, ny in get_near(cx, cy, n): # 움직일 수 있는 좌표를 우선순위큐에 저장
            if not visited[ny][nx] and 0<=board[ny][nx]<=shark_size:
                heappush(hq, (dist+1, ny, nx)) 
                visited[ny][nx] = True
    return None, None

def main(board, n):
    for y in range(n):
        for x in range(n):
            if board[y][x]==9: # 상어 초기 위치 확인
                shark_loc = (x, y); board[y][x] = 0
                break
    shark_size, exp, time = 2, 0, 0
    while True:
        target, dist = choice(board, shark_loc, shark_size, n)
        if not target: # 잡아먹을 수 있는 물고기 없으면 끝냄
            return time
        time += dist # 거리만큼 시간이 걸림
        board[target[1]][target[0]] = 0; shark_loc = target # 물고기 잡아먹기
        if exp == shark_size-1: # 물고기 사이즈만큼 잡아먹으면 레벨업
            exp=0
            shark_size+=1
        else: # 물고기 사이즈 이하인 경우 경험치 += 1
            exp+=1

if __name__ == "__main__":
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    print(main(board, n))
