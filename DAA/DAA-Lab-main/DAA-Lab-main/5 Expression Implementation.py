a = [
    [3, 8, 4],
    [2, 9, 6],
    [8, 4, 9]
]


def summation():
    x = 0
    for i in range(3):
        for j in range(i + 1):
            x += a[i][j]
    return f'value of {x}'


def minimum():
    min_nums = []
    for i in range(3):
        min = a[i][0]
        for j in range(1,3):
            if min > a[i][j]:
                min = a[i][j]
        min_nums.append(min)
    return f'Result: {min_nums}'


def maximum():
    max_nums = []
    for j in range(3):
        max = a[j][0]
        for i in range(1, 3):
            if max < a[i][j]:
                max = a[i][j]
        max_nums.append(max)
    return f'Result: {max_nums}'


if __name__ == '__main__':
    print('1. ', summation())
    print('2. ', minimum())
    print('3. ', maximum())
