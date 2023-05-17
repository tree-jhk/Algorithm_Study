import sys
from itertools import product
input = lambda : map(int, sys.stdin.readline().split())
# cctv별 볼 수 있는 방향, 0123은 상우하좌
cctv = [[],[1],[1,3],[0,1],[0,1,3],[0,1,2,3]]

class Mover:
    """
    입력받은 n, m, walls, dx, dy를 고려
    호출 시 현재 좌표에서 어떠한 방향으로 볼 수 있는 모든 좌표를 yield
    """
    __slots__=['n', 'm', 'walls', 'dx', 'dy']
    def __init__(self, n, m, walls):
        self.n = n
        self.m = m
        self.walls = walls
        self.dx = (0,1,0,-1)
        self.dy = (-1,0,1,0)

    def __call__(self, x, y, direction):
        for i in range(8):
            nx, ny = x+i*self.dx[direction], y+i*self.dy[direction]
            if any([nx<0, ny<0, nx>=m, ny>=n, (nx,ny) in self.walls]):
                break # 벽이나 보드의 너비, 높이에 의해 시야각이 끊긴경우 break
            yield nx, ny # cctv가 볼 수 있는 좌표 yield

def turn(view:list, turnval:int):
    """ cctv의 방향(view)을 회전량(turnval)만큼 돌림 """
    for i in view:
        yield (i+turnval)%4

def count_nonviewable_sights(field):
    """ 사각지대의 개수를 리턴 """
    return sum(i.count(0) for i in field)

def solve(board, info, n, m):
    move = Mover(n, m, info[6])
    answer = float("inf")
    for case in product(range(4), repeat=len(info[1])): # cctv가 볼 수 있는 모든 방향에 대하여
        field = [[1 if (x,y) in info[6] else 0 for x in range(m)] for y in range(n)]
        for (x, y), cctv_turn_value in zip(info[1], case):
            """ 이 부분 누적합으로 가능해 보임. 안해도 느리지만 통과는 됨. """
            for cctv_dir in turn(cctv[board[y][x]], cctv_turn_value):
                for nx, ny in move(x, y, cctv_dir): # 보이는 곳은
                    field[ny][nx] = 1 # 1로 표현
        answer = min(answer, count_nonviewable_sights(field)) # 정답 갱신
    return answer

# cctv 8개 => 4**k
# cctv당 최대 시야각 : n+m
# O((n+m)*4**k) => 최악 O((16)*(4**8)) ~= 100만 꽤 널널함. 무지성 완탐
if __name__ =="__main__":
    n, m = input()
    board = [[0]*m for _ in range(n)]
    info = {i:set() for i in (0,1,6)} # 0: 빈칸, 1: cctv, 6: wall : 빠른 조회를 위한 set
    for y in range(n):
        for x, v in enumerate(input()):
            board[y][x] = v
            if v==6: # 벽은 6에 저장
                info[6].add((x,y))
            else: # 빈칸은 0에, cctv는 1에 저장
                info[min(1, v)].add((x,y))
    print(solve(board, info, n, m))

# # 2. 누적합 시간초과
# import sys
# from itertools import product, accumulate
# input = lambda : map(int, sys.stdin.readline().split())
# # cctv별 볼 수 있는 방향, 0123은 상우하좌
# cctv = [[],[1],[1,3],[0,1],[0,1,3],[0,1,2,3]]

# class Mover:
#     """
#     입력받은 n, m, walls, dx, dy를 고려
#     호출 시 현재 좌표에서 어떠한 방향으로 볼 수 있는 모든 좌표를 yield
#     """
#     __slots__=['n', 'm', 'walls', 'dx', 'dy']
#     def __init__(self, n, m, walls):
#         self.n = n
#         self.m = m
#         self.walls = walls
#         self.dx = (0,1,0,-1)
#         self.dy = (-1,0,1,0)

#     def __call__(self, x, y, direction, cnt=-1):
#         answer = None
#         for i in range(8):
#             nx, ny = x+i*self.dx[direction], y+i*self.dy[direction]
#             if any([nx<0, ny<0, nx>=m, ny>=n, (nx,ny) in self.walls]):
#                 return answer
#             answer = [nx, ny]
#         return answer
    
# def turn(view:list, turnval:int):
#     """ cctv의 방향(view)을 회전량(turnval)만큼 돌림 """
#     for i in view:
#         yield (i+turnval)%4

# def solve(board, info, n, m):
#     move = Mover(n, m, info[6])
#     answer = float("inf")
#     for case in product(range(4), repeat=len(info[1])): # cctv가 볼 수 있는 모든 방향에 대하여
#         field = [[0]*(m+1) for _ in range(n+1)]
#         for (x, y), cctv_turn_value in zip(info[1], case):
#             """ 이 부분 누적합으로 가능해 보임. 안해도 느리지만 통과는 됨. """
#             for cctv_dir in turn(cctv[board[y][x]], cctv_turn_value):
#                 _x, _y = move(x, y, cctv_dir)
#                 xmin, xmax = sorted([x, _x])
#                 ymin, ymax = sorted([y, _y])
#                 field[ymin][xmin] += 1
#                 field[ymax+1][xmax+1] += 1
#                 field[ymin][xmax+1] -= 1
#                 field[ymax+1][xmin] -= 1
#         field = [list(accumulate(i)) for i in field]
#         for x in range(m):
#             for y in range(1, n):
#                 field[y][x] += field[y-1][x]
#         for x, y in info[6]:
#             field[y][x] += 1
#         cnt = 0
#         for y in range(n):
#             for x in range(m):
#                 if field[y][x]==0:
#                     cnt += 1
#         answer = min(answer, cnt)
#     return answer

# if __name__ =="__main__":
#     n, m = input()
#     board = [[0]*m for _ in range(n)]
#     info = {i:set() for i in (0,1,6)}
#     for y in range(n):
#         for x, v in enumerate(input()):
#             board[y][x] = v
#             if v==6:
#                 info[6].add((x,y))
#             else:
#                 info[min(1, v)].add((x,y))
#     print(solve(board, info, n, m))