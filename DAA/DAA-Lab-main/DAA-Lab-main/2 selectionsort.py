def selectionSort(arr):
    print('Original array: ', arr)
    n = len(arr)
    count_steps = count_swaps = count_passes = 0
    for i in range(n):
        swapped = True
        count_passes += 1
        min_idx = i
        for j in range(i + 1, n):
            count_steps += 1
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        swapped = True
        count_swaps += 1
        if not swapped:
            break
    print('Sorted array: ', arr)
    print(f'{count_passes=}, {count_steps=}, {count_swaps=}')


arr = [45, 24, 13, 56, 36, 82]
selectionSort(arr)
