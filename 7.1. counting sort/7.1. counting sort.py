input = [5, 8, 4, 3, 7, 1, 5, 10]

def counting_sort():
    array = [0] * (max(input) + 1)
    for i in range(len(input)):
        array[input[i]] += 1
    for i in range(1, len(array)):
        array[i] += array[i - 1]
    out = [0] * len(input)
    for i in range(len(input) - 1, -1, -1): # we set this loop backward in order to make the program, stable
        out[array[input[i]] - 1] = input [i]
        array[input[i]] -= 1
    print(out)

counting_sort()