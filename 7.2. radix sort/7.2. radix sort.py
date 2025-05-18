array = ["0112", "0088", "3244", "0122", "3236", "8111"]

def radix_sort(x, input):
    if x < 0:
        print(input)
        return
    array = [0] * 10
    for i in range(len(input)):
        array[int(input[i][x])] += 1
    for i in range(1, len(array)):
        array[i] += array[i - 1]
    out = [0] * len(input)
    for i in range(len(input) - 1, -1, -1): # we set this loop backward in order to make the program, stable
        out[array[int(input[i][x])] - 1] = input [i]
        array[int(input[i][x])] -= 1
    radix_sort(x - 1, out)

    
radix_sort(len(array[0]) - 1, array)