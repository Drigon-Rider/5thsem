merge_sort_calls = merge_calls = 0


def merge(left: [int], right: [int]) -> [int]:
    global merge_calls
    merge_calls += 1
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result


def merge_sort(arr: [int]) -> [int]:
    global merge_sort_calls
    merge_sort_calls += 1
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)


if __name__ == "__main__":
    arr = [38, 27, 43, 3, 9, 82, 10, 25, 17, 30]
    print(f'Unsorted array: {arr}')
    print(f'Sorted array: {merge_sort(arr)}')
    print(f'Merge sort calls: {merge_sort_calls}')
    print(f'Merge calls: {merge_calls}')
