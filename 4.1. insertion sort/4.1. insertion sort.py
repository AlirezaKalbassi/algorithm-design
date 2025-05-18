input = [5, 4, 3, 3, 9, 8, 1, 2]

def insertion_sort():
    for i in range(1, len(input)):
        for j in range(i - 1, -1, -1):
            if input[j] > input[j + 1]:
                input[j], input[j + 1] = input[j + 1], input[j]
            else:
                break
    print (input)

insertion_sort()