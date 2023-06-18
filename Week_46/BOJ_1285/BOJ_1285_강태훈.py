import sys
from collections import Counter
input = lambda : sys.stdin.readline().rstrip()

def str2bin(str, n, l=0):
    for token in str:
        l<<=1
        if token=="H":
            l+=1
    return min(l, ((1<<n)-1)^l)

def count_1(num, cnt=0):
    while num:
        cnt += num&1
        num>>=1
    return cnt

def main(o_board, n, answer=float("inf")):
    board = Counter(o_board)
    for mask in range(1<<n):
        local = 0
        for line, size in board.items():
            cnt = count_1(line^mask)
            # print(f"{bin(line)} & {bin(mask)} = {bin(cnt)}")
            local += min(cnt, n-cnt)*size
        answer = min(answer, local)
    return answer

if __name__ == "__main__":
    n = int(input())
    board = [str2bin(input(), n) for _ in range(n)]
    print(main(board, n))
    