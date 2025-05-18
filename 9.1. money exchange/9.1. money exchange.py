d = [1, 4, 5]
r = [10, 60, 80]
money = 8 

def max_rial():
    dp = [0] * (money + 1)
    len_dp = [[0]] * (money + 1)
    for i in range(1, money + 1):
        for j in range(len(d)):
            if d[j] > i:
                break
            if r[j] + dp[i - d[j]] > dp[i]:
                dp[i] = r[j] + dp[i - d[j]]
                len_dp[i] = [d[j]] + len_dp[i - d[j]]
    print(len_dp[money])
    return dp[money]

print(max_rial())