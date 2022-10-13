def main():
    a = [1, 2, 3]
    b = a

    print(f"a == b = {a == b}")
    print(f"a is b = {a is b}")

    c = [1, 2, 3,]
    print(f"a == c = {a == c}")
    print(f"a is c = {a is c}")


if __name__ == "__main__":
    main()