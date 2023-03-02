def seed(value):
    result = 0
    for i in range(len(value)):
        result += int(value[i])
    return str(result % 2)


def main(n):
    for i in range(1, n):
        binary = format(i, 'b')

        binary += seed(binary)
        binary += seed(binary)

        result = int(binary, 2)

        if result > 77:
            print(result)
            break


if __name__ == '__main__':
    main(100)
