input = [5, 4, 3, 9, 8, 1, 2]

def selection_sort():
    for i in range(len(input)):
        index = 0
        min = 1000
        for j in range(i, len(input)):
            if input[j] < min:
                min = input[j]
                index = j
        input[i], input[index] = input[index], input[i]
    print(input)
    
selection_sort()