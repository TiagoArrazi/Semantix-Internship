class FooBar:

    def __init__(self, foo, bar):
        self.foo = foo
        self.bar = bar


obj = FooBar('obj_foo', 'obj_bar')
print(obj.foo)

obj.foo = 'not_a_foo'
print(obj.foo)
