input = [int (x) for x in input().split()]

def merge_sort(i, j):
    if i == j:
        return [input[i]]
    mid = (i + j) // 2
    lefthalf = merge_sort(i, mid)
    righthalf = merge_sort(mid + 1, j)
    array = merge_halves(lefthalf, righthalf)
    return array

def merge_halves(lefthalf, righthalf):
    i, j = 0, 0
    array = []
    for _ in range(len(lefthalf) + len(righthalf)):
        if lefthalf[i] < righthalf[j]:
            array.append(lefthalf[i])
            if i+1 == len(lefthalf): # for preventing out of range error1
                array += righthalf[j:]
                return array
            else:
                i += 1
        else:
            array.append(righthalf[j])
            if j+1 == len(righthalf):
                array += lefthalf[i:]
                return array
            else:
                j += 1
    return array

print (merge_sort(0, len(input) - 1))