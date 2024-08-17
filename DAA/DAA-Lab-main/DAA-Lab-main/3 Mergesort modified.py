import heapq
divide = []
merging = []


def merge(left: [int], right: [int], level: int) -> [int]:
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
    heapq.heappush(merging, (level, f'{left} {right}=>{result}'))
    return result


def merge_sort(arr: [int], level: int) -> [int]:
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    heapq.heappush(divide, (level, f'{arr[:mid]} {arr[mid:]}'))
    left = merge_sort(arr[:mid], level + 1)
    right = merge_sort(arr[mid:], level + 1)
    return merge(left, right, level)


if __name__ == "__main__":
    arr = [38, 27, 43, 3, 9, 82, 10, 25, 17, 30]
    heapq.heappush(divide, (0, str(arr)))
    sorted_arr = merge_sort(arr, 1)
    print('Dividing:')
    lvl = 0
    while divide:
        i = heapq.heappop(divide)
        if i[0] > lvl:
            lvl = i[0]
            print()
        print(i[1], end=' ')
    print('\n\nMerging:')
    li = heapq.nlargest(len(merging), merging)
    for i in li:
        print(i[1])
