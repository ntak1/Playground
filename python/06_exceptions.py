from abc import ABCMeta, abstractmethod

class Abstract():
    def abstract_method(self):
        raise NotADirectoryError()


class Base(metaclass=ABCMeta):
    @abstractmethod
    def foo(self):
        pass

    @abstractmethod
    def bar(self):
        pass

class Concrete(Base):
    def foo(self):
        pass


def main():
    assert issubclass(Concrete, Base)
    concrete = Concrete()


if __name__ == "__main__":
    main()