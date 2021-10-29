def main(n):
    Sum = 0
    for i in range(n):
        if i % 3 == 0 or i % 5 == 0:
            Sum += i
    return Sum


if __name__ == '__main__':
    print(main(1000))
