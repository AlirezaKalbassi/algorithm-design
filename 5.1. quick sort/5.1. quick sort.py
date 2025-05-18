from random import randrange
input = [5, 4, 7, 9, 2, 8, 6, 3]

def choose_random_pivot(start, end):
    r = randrange(start, end)
    input[r], input[start] = input[start], input[r]

def quick_sort(start, end):
    if end - start <= 0:
        return
    choose_random_pivot(start, end) # optional, for improving the time order
    p = start
    i = p + 1
    for j in range(p + 1, end + 1):
        if input[j] < input[p]:
            if i != j:
                input[i], input[j] = input[j], input[i]
            i += 1
    input[p], input[i - 1] = input[i - 1], input[p]
    quick_sort(start, i - 2) # p = i - 1 and we need p - 1 and p + 1
    quick_sort(i, end)
    
quick_sort(0, len(input) - 1)
print (input)