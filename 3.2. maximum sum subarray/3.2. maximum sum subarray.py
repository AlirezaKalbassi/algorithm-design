input = [3, -5, 5, -2, 4, -5, -2, 6]

def max_sum(start, end):
    if start == end:
        return input[start]
    lmax, rmax, lsum, rsum = 0, 0, 0, 0
    mid = (start + end) // 2
    left_half = max_sum(start, mid)
    right_half = max_sum(mid + 1, end)
    for i in range(mid, start - 1, -1):
        lsum += input[i]
        if lsum > lmax:
            lmax = lsum
    for i in range(mid + 1, end + 1):
        rsum += input[i]
        if rsum > rmax:
            rmax = rsum
    return max(left_half, right_half, lmax + rmax)

print(max_sum(0, len(input) - 1))