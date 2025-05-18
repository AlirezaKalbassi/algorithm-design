input = [2, 3, 5, 6, 9]
money = 10

def min_coin():
    dp = [money + 1] * (money + 1)
    dp[0] = 0
    for i in range(1, money + 1):
        for j in range(len(input)):
            if input[j] > i:
                break
            if 1 + dp[i - input[j]] < dp[i]:
                dp[i] = 1 + dp[i - input[j]]
    if dp[money] > money:
        return "we can't change the money"
    return dp[money]

print(min_coin())