import random
totalStep = 0


def binarySearch(arr, l, r, key):
    if r >= l:
        mid = l + (r - l) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] > key:
            return binarySearch(arr, l, mid - 1, key)
        elif arr[mid] < key:
            return binarySearch(arr, mid + 1, r, key)
    else:
        return -1


def main():
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    key = 5
    print(f"Element found at index {binarySearch(arr,0, len(arr) - 1, key)}")


def modifiedBinarySearch(arr, l, r, key, step):
    while l <= r:
        mid = l + (r - l) // 2
        if arr[mid] == key:
            return mid, step
        elif arr[mid] < key:
            return modifiedBinarySearch(arr, mid + 1, r, key, step + 1)
        elif arr[mid] > key:
            return modifiedBinarySearch(arr, l, mid - 1, key, step + 1)
    return -1, 0


def modifiedMain():
    global totalStep
    count = 0
    arr = [i for i in range(1, 1001)]
    keys = [random.randint(1, 2000) for _ in range(100)]
    for key in keys:
        index, step = modifiedBinarySearch(arr, 0, len(arr) - 1, key, 1)
        if index != -1:
            count += 1
        totalStep += step
    averageStep = totalStep / count
    print(f'Average steps: {averageStep:.2f}')
    print(f'Count: {count}')


if __name__ == '__main__':
    modifiedMain()

