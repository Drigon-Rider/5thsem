def insertionSort(arr):
    print('Original array: ', arr)
    n = len(arr)
    count_steps = count_swaps = count_passes = 0
    for i in range(1, n):
        swapped = False
        count_passes += 1
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            count_steps += 1
            arr[j + 1] = arr[j]
            j -= 1
            count_swaps += 1
            swapped = True
        arr[j + 1] = key
        if not swapped:
            break
    print('Sorted array: ', arr)
    print(f'{count_passes=}, {count_steps=}, {count_swaps=}')


arr = [45, 24, 13, 56, 32, 82]
insertionSort(arr)
