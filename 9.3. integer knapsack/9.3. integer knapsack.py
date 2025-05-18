p = [10, 100, 120] #price
w = [10, 20, 30] #weight
weight = 50

def max_weight():
    dp = [0] * (weight // w[0] + 1)
    weight_dp = [[0]] * (weight // w[0] + 1)
    for i in range(1 * w[0], len(dp) * w[0], w[0]):
        for j in range(len(p)):
            if w[j] > i:
                break
            if p[j] + dp[(i - w[j]) // w[0]] > dp[i // w[0]]:
                dp[i // w[0]] = p[j] + dp[(i - w[j]) // w[0]]
                weight_dp[i // w[0]] = [w[j]] + weight_dp[(i - w[j]) // w[0]]
    print(weight_dp[len(dp) - 1])
    return dp[len(dp) - 1]

print(max_weight())