from functools import lru_cache


@lru_cache(maxsize=2)
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)


def main():
    k = 0
    Sum = 0
    while fib(k) < 4000000:
        if fib(k) % 2 == 0:
            Sum += fib(k)
        k += 1
    return Sum


if __name__ == '__main__':
    print(main())
