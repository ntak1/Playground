

def uppercase(func):
    def wrapper():
        original_result = func()
        modified_result = original_result.upper()
        return modified_result
    return wrapper


@uppercase
def print_hello():
    return "Hello World!"


def main():
    print(print_hello())


if __name__ == "__main__":
    main()
