input = [1, 3, 4, 5, 8]
lenth = len(input)

def rod_cut(): 
    dp = [0] * (lenth + 1)
    len_dp = [[0]] * (lenth + 1)
    for i in range(1, lenth + 1):
        for j in range(1, i + 1):
            if input[j - 1] + dp[i - j] > dp[i]:
                dp[i] = input[j - 1] + dp[i - j]
                len_dp[i] = [j] + len_dp[i - j]
    print(len_dp[lenth])
    return dp[lenth]

print(rod_cut())