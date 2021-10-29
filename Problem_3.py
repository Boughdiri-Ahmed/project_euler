import math as m


def is_prime(n):
    for i in range(2, int(m.sqrt(n))):
        if n % i == 0:
            return False
    return True


def get_prime_factors(n):
    prime_factors = []
    for i in range(2, int(m.sqrt(n))):
        if n % i == 0 and is_prime(i):
            prime_factors.append(i)
    return prime_factors


def main(n):
    return max(get_prime_factors(n))


if __name__ == '__main__':
    print(main(600851475143))
