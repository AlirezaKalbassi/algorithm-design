input = [3, 1, 4, 5, 4, 1]

dp = [0] * len(input)
dp_mem = [0] * len(input)

def mis():
    dp[0], dp[1] = input[0], input[1]
    max = 0
    index = 0
    for i in range(len(input)):
        for j in range(i-1):
            if input[i] + dp[j] > dp[i]:
                dp[i] = input[i] + dp[j]
                dp_mem[i] = j
        if dp[i] > max:
            max = dp[i]
            index = i
    print(mis_print(index))
    return max

def mis_print(i):
    if dp[i] == input[i]:
        return str(input[i])
    else:
        return mis_print(dp_mem[i]) + " " + str(input[i])

print(mis())