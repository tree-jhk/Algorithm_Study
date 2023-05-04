import sys
input = sys.stdin.readline


def main(mems, costs, n, m):
    if n==1:
        return costs[0]
    total_cost, result = sum(costs), float("inf")
    dp = [[0]*(total_cost) for _ in range(n)]

    for p in range(n):
        for w in range(total_cost):
            if costs[p] > w:
                dp[p][w] = dp[p-1][w]
            else:
                dp[p][w] = max(dp[p-1][w], mems[p]+dp[p-1][w-costs[p]])
            if dp[p][w] >= m:
                result = min(result, w)
                break
    return result if result!=float("inf") else n*m

if __name__ == "__main__":
    n, m = map(int, input().split())
    mems = list(map(int, input().split()))
    costs = list(map(int, input().split()))
    print(main(mems, costs, n, m))