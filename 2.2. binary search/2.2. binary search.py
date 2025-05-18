input = [1, 3, 5, 7, 9, 10]
number = 10

def binary_search(start, end):
    mid = (start + end) // 2
    if input[mid] == number:
        print (mid)
        return
    if start == end:
        print("the list doesn't contain the number you want")
        return
    if input[mid] > number:
        binary_search(start, mid - 1)
    else:
        binary_search(mid + 1, end)

binary_search(0, len(input) - 1)