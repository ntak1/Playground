def assert_simple():
    assert False, "Custom error message"


def assert_with_expression():
    assert False, print("Hello")


if __name__ == "__main__":
    assert_with_expression()
