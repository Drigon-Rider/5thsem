import random

totalStep = 0
count = 0


def modifiedLinearSearch(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i, i+1
    return -1, 0


def modifiedMain():
    global totalStep
    global count
    arr = [i for i in range(1000, 0, -1)]
    keys = [random.randint(1, 2000) for _ in range(50000)]
    for key in keys:
        index, step = modifiedLinearSearch(arr, key)
        if index != -1:
            count += 1
        totalStep += step
    averageStep = totalStep / count
    print(f'Average steps: {averageStep}')
    print(f'Count: {count}')


def linearSearch(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1


def main():
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    key = 5
    print(f"Element found at index {linearSearch(arr, key)}")


if __name__ == '__main__':
    modifiedMain()
