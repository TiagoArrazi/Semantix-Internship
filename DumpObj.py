from inspect import getmembers

class FooBar:

    def __init__(self, foo, bar):
        self.foo = foo
        self.bar = bar


obj = FooBar('tar', 'ball')

print(getmembers(obj))
