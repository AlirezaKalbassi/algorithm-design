input = ['b', 'b', 'a', 'b', 'c', 'b', 'c', 'a', 'd']

dp = [[1] * len(input) for _ in range(len(input))]
dp_mem = [[0] * len(input) for _ in range(len(input))]

def lps():
    for i in range(len(input) - 1): # setting main values
        if input[i] == input[i + 1]:
            dp[i][i + 1] = 2
    for x in range(2, len(input)):
        for i in range(len(input) - x):
            j = i + x
            if input[i] == input[j]:
                dp[i][j] = 2 + dp[i + 1][j - 1]
            else:
                dp[i][j] = dp[i + 1][j] 
                if dp[i][j - 1] > dp[i + 1][j]:
                    dp[i][j] = dp[i][j - 1] 
                    dp_mem[i][j] = 1

    print(lps_printer(0, len(input) - 1))
    return dp[0][len(input) - 1]

def lps_printer(i, j):
    if j - i < 0:
        return ""
    elif i == j:
        return input[i]
    if input[i] == input[j]:
        return input[i] + lps_printer(i + 1, j - 1) + input[j]
    elif dp_mem[i][j] == 1:
        return lps_printer(i, j - 1)
    else:
        return lps_printer(i + 1, j)

print(lps())