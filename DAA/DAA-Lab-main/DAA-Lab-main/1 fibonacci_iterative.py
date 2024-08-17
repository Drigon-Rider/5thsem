# Fibonacci series using iterative method
def fibonacci(n: int):
    a, b = 0, 1
    for _ in range(n - 2):
        a, b = b, a + b
    return b


if __name__ == '__main__':
    print(f'{fibonacci(5)=}')
    