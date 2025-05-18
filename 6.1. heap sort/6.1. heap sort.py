input = [1, 3, 7, 6, 9, 5] 

def heapify(i, n):
    if n < 2 * i + 1 and n < 2 * i + 2:
        return
    max = 2 * i + 1
    if max + 1 <= n and input[max + 1] > input[max]:
        max += 1
    if input[max] < input[i]:
        return
    input[max], input[i] = input[i], input[max]
    heapify(max, n)
    
def build_max_heap():
    n = len(input) - 1
    for i in range(n//2, -1, -1):
        heapify(i, n)

def heap_sort():
    build_max_heap()
    for i in range(len(input) - 1, 0, -1):
        input[i], input[0] = input[0], input[i]
        heapify(0, i - 1)
    print(input)
   
heap_sort()