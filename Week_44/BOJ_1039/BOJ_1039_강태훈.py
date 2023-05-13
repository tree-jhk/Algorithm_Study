import sys
from heapq import heappush, heappop
input = lambda : sys.stdin.readline().rstrip()

def main(n, k, size):
    hq = [(0, -n)]
    visited = set()
    while hq:
        cnt, number = heappop(hq)
        if cnt==k:
            return -number
        for i in range(size):
            for j in range(i+1, size):
                temp = list(str(-number))
                if temp[j]=="0" and i==0:
                    continue
                temp[i], temp[j] = temp[j], temp[i]
                next_case = (cnt+1, -int("".join(temp)))
                if next_case not in visited:
                    visited.add(next_case)
                    heappush(hq, next_case)

    return -1

if __name__ == "__main__":
    n, k = input().split()
    print(main(int(n), int(k), size=len(n)))