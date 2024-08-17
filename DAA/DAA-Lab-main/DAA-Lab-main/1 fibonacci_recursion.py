# Fibonacci series using recursion
def fibonacci(n: int):
    if n == 2:
        return 1
    elif n == 1:
        return 0
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == '__main__':
    print(f'{fibonacci(4)=}')
