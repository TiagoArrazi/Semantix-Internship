from inspect import getmembers


attributes = {'__FooBar__': ['foo', 'bar'],
              '__Sigma__': ['alpha', 'beta', 'gamma']}

class Jsonifier:

    @classmethod
    def jsonify_obj(cls, obj, _repr):

        serialized = {}
        global attributes

        for attr in dir(obj):
            if attr in attributes[_repr]:
                serialized[attr] = getattr(obj, attr)

        return serialized


class FooBar:

    def __init__(self, foo, bar):
        self.foo = foo
        self.bar = bar

    @classmethod
    def __repr__(cls):
        return '__FooBar__'


class Sigma:

    def __init__(self, alpha, beta, gamma):
        self.alpha = alpha
        self.beta = beta
        self.gamma = gamma


    @classmethod
    def __repr__(cls):
        return '__Sigma__'


foobar_1 = FooBar('tar', 'ball')
foobar_2 = FooBar('shell', 'bash')

sigma_1 = Sigma('a', 'b', 'c')
sigma_2 = Sigma('A', 'B', 'C')

print([Jsonifier.jsonify_obj(obj, obj.__repr__()) for obj in [foobar_1, foobar_2]])
print([Jsonifier.jsonify_obj(obj, obj.__repr__()) for obj in [sigma_1, sigma_2]])
