if __name__ == "__main__":
    N, M = map(int, input().split())
    nums = [0] + list(map(int, input().split()))
    costs = [0] + list(map(int, input().split()))
    
    sumCost = sum(costs)
    dp = [[0] * (sumCost + 1) for _ in range(N + 1)]
    
    result = 1000000001 # sum(nums) + 1
    for i in range(1, N + 1):
        byte = nums[i]
        cost = costs[i]
        for j in range(1, sumCost + 1):
            if j < cost:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j - cost] + byte, dp[i - 1][j])
            if dp[i][j] >= M:
                result = min(result, j)

    if result == 1000000001:
        print(sumCost)
    else:
        print(result)