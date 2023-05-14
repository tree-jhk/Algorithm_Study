def canmove(board, smell, x, y):
    if out(x, y):
        return False
    if board[x][y] == -1 or smell[x][y] == -2:
        return False
    return True

def out(x, y):
    if x >= 4 or x < 0 or y >= 4 or y < 0:
        return True
    return False

if __name__ == "__main__":
    M, S = map(int, input().split())
    
    board = [[0] * 4 for _ in range(4)] # 물고기 수
    smell = [[0] * 4 for _ in range(4)]
    shark = [[0] * 4 for _ in range(4)]
    dx = [0, -1, -1, -1, 0, 1, 1, 1]
    # dx = [1, 1, 1, 0, -1, -1, -1, 0]
    dy = [-1, -1, 0, 1, 1, 1, 0, -1]
    # dy = [-1, 0, 1, 1, 1, 0, -1, -1]
    flist = []
    initFish = []
    for _ in range(M):
        fx, fy, d = map(int, input().split())
        board[fx - 1][fy - 1] += 1
        flist.append([fx - 1, fy - 1, d - 1])
        initFish.append([fx - 1, fy - 1, d - 1])
    
    sx, sy = map(int, input().split())
    sx -= 1
    sy -= 1
    shark[sx][sy] = -1
    
    for _ in range(S):
        initFish = flist
        # # 1. 복제 마법 시전
        # [print(b) for b in board]
        # print()
        # 2. 모든 물고기가 한 칸 이동
        for i in range(len(flist)):
            x, y, d = flist[i]
            nx = x + dx[d]
            ny = y + dy[d]
            flag = False
            # 상어가 있는 칸(-1), 물고기 냄새가 있는 칸(-2),
            # 격자의 범위를 벗어나는 칸으로는 이동할 수 없다.
            if not canmove(board, smell, nx, ny):
                # 이동할 수 있을 때까지 방향을 45도 반시계 회전
                for k in range(1, 8):
                    nnx = x + dx[(d - k) % 8]
                    nny = y + dy[(d - k) % 8]
                    if canmove(board, smell, nnx, nny):
                        flist[i][2] = (d - k) % 8
                        d = (d - k) % 8
                        nx = nnx
                        ny = nny
                        flag = True # 이동 가능
                        break
            else: flag = True
            
            # 이동
            if flag:    # 이동할 수 없다면 이동 x
                board[nx][ny] += 1
                board[x][y] -= 1
                flist[i][0] = nx
                flist[i][1] = ny
        
        # 4. 상어가 3칸 이동
        dx4 = [-1, 0, 1, 0] # 상 좌 하 우
        dy4 = [0, -1, 0, 1]
        fish = 0
        maxFish = 0
        sharkPath = []
        for i in range(4):
            onex = sx + dx4[i]
            oney = sy + dy4[i]
            if out(onex, oney):
                continue
            onetmp = smell[onex][oney]
            fish1 = 0
            if board[onex][oney] > 0 and smell[onex][oney] == 0:
                fish1 = board[onex][oney]
                # print("1 fish", fish, "at", onex, oney)
                smell[onex][oney] = 2
                # board[onex][oney] = -2
            for j in range(4):
                twox = onex + dx4[j]
                twoy = oney + dy4[j]
                if out(twox, twoy):
                    continue
                twotmp = smell[twox][twoy]
                fish2 = fish1
                if board[twox][twoy] > 0 and smell[twox][twoy] == 0:
                    fish2 = fish1 + board[twox][twoy]
                    # print("2 fish", fish, "at", twox, twoy)
                    # board[twox][twoy] = -2
                    smell[twox][twoy] = 2
                for k in range(4):
                    # print("three!!")
                    threex = twox + dx4[k]
                    threey = twoy + dy4[k]
                    # print(threex, threey)
                    if out(threex, threey):
                        continue
                    threetmp = smell[threex][threey]
                    # [print(b) for b in smell]
                    # print()
                    fish3 = fish2
                    if board[threex][threey] > 0 and smell[threex][threey] == 0:
                        # print("here")
                        fish3 = fish2 + board[threex][threey]
                        # print("???",board[threex][threey])
                        # print("3 fish", fish, "at", threex, threey)
                        # board[threex][threey] = -2
                        smell[threex][threey] = 2
                        # [print(b) for b in smell]
                        # # print("fish", fish3)
                        # print()
                        # [print(b) for b in board]
                        # print()
                    if maxFish < fish3:
                        print(i, j, k)
                        
                        # print(fish)
                        maxFish = fish3
                        sharkPath = [[onex, oney], [twox, twoy], [threex, threey]]
                    
                    # board[threex][threey] = threetmp
                    smell[threex][threey] = threetmp
                    # fish = 0
                
                # board[twox][twoy] = twotmp
                smell[twox][twoy] = twotmp
            # board[onex][oney] = onetmp
            smell[onex][oney] = onetmp
        # print("shark",sharkPath)
        # 상어가 지나간 자리에 물고기 있었다면 물고기 냄새
        
        # [print(b) for b in board]
        # print()
        nFlist = []
        for i in range(len(sharkPath)):
            if board[sharkPath[i][0]][sharkPath[i][1]] > 0:
                smell[sharkPath[i][0]][sharkPath[i][1]] = 2
                board[sharkPath[i][0]][sharkPath[i][1]] = 0
                # 없어진 물고기 flist에서 지우기
                for j in range(len(flist)):
                    if flist[j][0] == sharkPath[i][0] and flist[j][1] == sharkPath[i][1]:
                        continue
                    nFlist.append(flist[j])
        flist = nFlist
        
        shark[sharkPath[-1][0]][sharkPath[-1][1]] = -1
        # [print(b) for b in board]
        # print()
        shark[sx][sy] = 0
        
        sx = sharkPath[-1][0]
        sy = sharkPath[-1][1]
        
        # 5. 복제 마법 완료
        for i in range(len(initFish)):
            flist.append(initFish[i])
            board[initFish[i][0]][initFish[i][1]] += 1

        [print(b) for b in board]
        print()
        # print(flist)
        # print()
    answer = len(flist)
   