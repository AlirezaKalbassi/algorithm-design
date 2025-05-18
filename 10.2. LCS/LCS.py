def lcs(array1, array2):
    dp = [[0] * (len(array2)) for _ in range(len(array1))]
    dp_print = [[0] * (len(array2)) for _ in range(len(array1))]
    
    for i in range(len(array1)):
        for j in range(len(array2)):
            if array1[i] == array2[j]:
                if i>0 and j>0:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1
                dp_print[i][j] = 1
            elif (j == 0 or dp[i - 1][j] > dp[i][j - 1]) and i != 0:
                dp[i][j] = dp[i - 1][j]
                dp_print[i][j] = 2
            else:
                dp[i][j] = dp[i][j - 1]
                dp_print[i][j] = 3

    def print_subarray(n, m):
        if n < 0 or m < 0:
            return ''
        if dp_print[n][m] == 1:
            return print_subarray(n - 1, m - 1) + array1[n]
        elif dp_print[n][m] == 3:
            return print_subarray(n, m - 1)
        else:
            return print_subarray(n - 1, m)
    
    return print_subarray(len(array1) - 1, len(array2) - 1)