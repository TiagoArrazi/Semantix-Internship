class Foo:

    def __init__(self, val_1, val_2, result):
        self.val_1 = val_1
        self.val_2 = val_2
        self.result = result

    def soma(self):
        return Foo(0, 0, self.val_1 + self.val_2)

    def print(self):
        print(self.result)


f = Foo(1, 1, 0)
f.soma().print()
