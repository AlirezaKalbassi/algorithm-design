input = [4, 5, 6, 3, 6, 8, 1, 5]
maximum = 0

def maxpro(start, end):
    global maximum
    mid = (start + end) // 2 
    if end == start:
        return [input[start], input[end]]
    lefthalf = maxpro(start, mid) # lefthalf = [min, max]
    righthalf = maxpro(mid + 1, end) # righthalf = [min, max]
    if righthalf[1] - lefthalf[0] > maximum:
        maximum = righthalf[1] - lefthalf[0]
    return [min(lefthalf[0], righthalf[0]) , max(lefthalf[1], righthalf[1])]

maxpro(0, len(input) - 1)
print (maximum)