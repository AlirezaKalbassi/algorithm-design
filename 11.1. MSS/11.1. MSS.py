input = [3, -4, 5, -2, -1, 3, 2, -7, 6]

dp = [0] * len(input)

def mss():
    dp[0] = input[0]
    maximum = 0
    index = 0
    for i in range(1, len(input)):
        dp[i] = max(input[i] + dp[i - 1], input[i])
        if dp[i] > maximum:
            maximum = dp[i]
            index = i
    print(print_mss(index))
    return maximum

def print_mss(i):
    if dp[i] == input[i] + dp[i - 1]:
        return print_mss(i-1) + " " + str(input[i])
    else:
        return str(input[i])

print(mss())