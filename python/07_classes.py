from collections import namedtuple


class MyClass:
    def instance_method(self):
        print("Instance method called")

    @classmethod
    def class_method(cls):
        print("Class method called")

    @staticmethod
    def static_method():
        print("Static method called")


def main():
    # Namedtuple
    Car = namedtuple("Car", ["color", "mileage"])
    my_car = Car("yellow", 0)
    print(my_car)

    # Class
    my_obj = MyClass()
    my_obj.instance_method()
    MyClass.class_method()
    MyClass.static_method()


if __name__ == "__main__":
    main()