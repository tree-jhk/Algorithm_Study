import sys
from collections import Counter
from itertools import product
from copy import deepcopy

input = sys.stdin.readline
# 물고기 이동방향
dx = (-1,-1, 0, 1, 1, 1, 0,-1)
dy = ( 0,-1,-1,-1, 0, 1, 1, 1)

# 상좌하우, 상어 이동방향
s_dx = (0,-1,0,1)
s_dy = (-1,0,1,0)

def check_movable(x, y, shark=(0,0), smell=set()):
    return all([0<x<5, 0<y<5, (x,y)!=shark, (x,y) not in smell])

def move_fish(fx, fy, d, shark, smell):
    iteration = list(range(d,0,-1))+list(range(8,d,-1))
    for direction in iteration:
        nx, ny = fx+dx[direction-1], fy+dy[direction-1]
        if check_movable(nx, ny, shark, smell):
            return (nx, ny, direction)
    return (fx, fy, d)

def show(f):
    board = [[[] for _ in range(4)] for _ in range(4)]
    for fish_info, cnt in f.items():
        x, y, direction = fish_info
        board[y-1][x-1].append(f"{direction}*{cnt}")
    for l in board:
        print(*l)

def simulation(s, f, shark, smell_1=set(), smell_2=set(), debug=True):
    if debug:
        print("INIT")
        show(f)
    for _ in range(s):
        # 1. 복제마법 준비
        o_f = deepcopy(f)
        # 2. 물고기 움직이기
        n_f = Counter()
        current_smell = smell_1.union(smell_2)
        for i, j in f.items():
            n_f[move_fish(*i, shark, current_smell)] += j
        # 3. 상어 움직이기
        remove_count = -1
        selected_route = (-1,-1)
        killed_fish = []
        for cmd in product(range(4), repeat=3):
            x, y = shark
            shark_footprint = set()
            for direction in cmd:
                nx, ny = x+s_dx[direction], y+s_dy[direction]
                if check_movable(nx, ny):
                    shark_footprint.add((nx, ny))
                    x, y = nx, ny
                else:
                    break
            else:
                cnt = 0
                killed = []
                for fish_info, number_of_fish in n_f.items():
                    if (fish_info[0], fish_info[1]) in shark_footprint:
                        killed.append(fish_info)
                        cnt += number_of_fish
                if cnt > remove_count:
                    remove_count = cnt
                    selected_route = (x, y)
                    killed_fish = killed
        # 상어 이동
        shark = selected_route
        # 3. 물고기 죽이고
        for fish_info in killed_fish:
            del n_f[fish_info]
        # 4. 냄새 남기고 (사라지고)
        smell_2 = deepcopy(smell_1)
        smell_1 = set([tuple(i[:2]) for i in killed_fish])
        # 5. 복제마법 완료
        f = n_f + o_f
        if debug:
            print(f"ROUND {_}")
            print(f"SHARK is located in {shark}")
            show(f)
    return sum(f.values())

if __name__ == "__main__":
    m, s = map(int, input().split())
    _f = [tuple(map(int, input().split())) for _ in range(m)]
    f = Counter([(i[1],i[0],i[2]) for i in _f])
    shark = tuple(map(int, input().split()))
    print(simulation(s, f, (shark[1], shark[0]), debug=False))