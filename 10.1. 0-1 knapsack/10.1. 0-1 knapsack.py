p = [10, 130, 120]
w = [10, 20, 30]
weight = 40


def max_weight():
    dp = [[0] * (weight // w[0] + 1) for _ in range(len(p))]
    global weight_holder
    weight_holder = [[0] * (weight // w[0] + 1) for _ in range(len(p))]
    maximum = 0
    for i in range(len(p)):
        for j in range(1, weight // w[0] + 1):
            dp[i][j] = dp[i - 1][j]
            if p[i] + dp[i - 1][j - w[i] // w[0]] > dp[i - 1][j] and j >= (w[i] // w[0]):
                dp[i][j] = p[i] + dp[i - 1][j - w[i] // w[0]]
                weight_holder[i][j] = 1
    weight_printer(i, j)
    return dp[len(p) - 1][weight // w[0]]

def weight_printer(i, j):
    if i < 0:
        return ""
    if weight_holder[i][j] == 1:
        print(w[i])
        weight_printer(i - 1, j - w[i] // w[0])
    else:
        weight_printer(i - 1, j)

print(max_weight())