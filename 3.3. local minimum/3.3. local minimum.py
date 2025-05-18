input = [1, 7, 2, 4, 5, 3, 6, 8, 10]

def local_min(start, end):
    if start == end:
        return input[start]
    mid = (start + end) // 2
    lmin = local_min(start, mid)
    rmin = local_min(mid + 1, end)
    if lmin < rmin:
        return lmin
    else:
        return rmin

print (local_min(0, len(input) - 1))