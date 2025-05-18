input = ['a', 'b', 'b', 'c', 'c', 'b', 'b', 'd']

dp = [[len(input) + 1] * len(input) for _ in range(len(input))]
dp_mem = [[0] * len(input) for _ in range(len(input))]

def min_pal():
    for j in range(len(input)):
        for i in range(len(input) - j):
            if input[i] == input[i + j] and dp[i - 1][i + j - 1]:
                dp[i][i + j] = 1
            else:
                for k in range(i, i + j):
                    if dp[i][k] + dp[k + 1][i + j] < dp[i][i + j]:
                        dp[i][i + j] = dp[i][k] + dp[k + 1][i + j]
                        dp_mem[i][i + j] = k
    print(pol_printer(0, len(input) - 1))
    return dp[0][len(input) - 1]

def pol_printer(i, j):
    if dp[i][j] == 1:
        return input[i:j + 1]
    else:
        return pol_printer(i, dp_mem[i][j]) + [" : "] + pol_printer(dp_mem[i][j] + 1, j)

print(min_pal())