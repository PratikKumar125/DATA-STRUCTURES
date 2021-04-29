'''
arr = [3, 34, 4, 12, 5, 2]
sum = 9
n = len(arr)
dp = ([[False for i in range(sum + 1)] for i in range(n+1)])
for i in range(0, n + 1):
    dp[i][0] = True
for i in range(1, sum + 1):
    dp[0][i] = False
for i in range(1, n + 1):
    for j in range(1, sum + 1):
        if arr[i - 1] <= j:
            dp[i][j] =  (dp[i - 1][j] or dp[i - 1][j - arr[i - 1]])
        else:
            dp[i][j] = dp[i - 1][j]
for i in dp:
    print(i)
'''

'''
# 0/1 knapsack
arr = [1, 2, 3, 4, 6]
val = [2, 4, 5, 1, 1]
n = len(arr)
sum = 8
dp = [[0 for i in range(sum + 1)] for i in range(len(arr) + 1)]
for i in range(1, n + 1):
    for j in range(sum + 1):
        if val[i - 1] > j:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j], arr[i - 1] + dp[i - 1][j - val[i - 1]])
print(dp[n][sum])
'''

















































