def make_adder(n):
    def add(x):
        return x + n
    return add


def main():
    num = 10

    add_3 = make_adder(3)
    print(add_3(num))

    add_4 = make_adder(4)
    print(add_4(num))


if __name__ == "__main__":
    main()