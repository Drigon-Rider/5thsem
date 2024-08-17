def bubbleSort(arr):
    print('Original array: ', arr)
    n = len(arr)
    count_steps = count_swaps = count_passes = 0
    for i in range(n):
        swapped = False
        count_passes += 1
        for j in range(0, n - i - 1):
            count_steps += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                count_swaps += 1
                swapped = True
        if not swapped:
            break
    print('Sorted array: ', arr)
    print(f'{count_passes=}, {count_steps=}, {count_swaps=}')


arr = [45, 24, 13, 56, 36, 82]
bubbleSort(arr)
