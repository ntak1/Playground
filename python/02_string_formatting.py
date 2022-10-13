from string import Template


def main():
    # Template strings for user input
    template = "Hey, $name. Welcome!"
    name = "Dummy"
    print(Template(template).substitute(name=name))

    # Literal String Interpolation
    num = 1000
    example = f"Hello this is an hex number={num:#x}, num={num:#X}, num={num:#o}"
    print(example)

    num = 10.123
    example = f"num={num:.2f}"
    print(example)


if __name__ == "__main__":
    main()