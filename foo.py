class Foo:

    def __init__(self, alpha='', kappa=0):
        self.alpha = alpha
        self.kappa = kappa

    def __repr__(self):
        return '<Foo: {} {}>'.format(self.alpha, self.kappa)

    def __str__(self):
        return 'Foo: {} {}'.format(self.alpha, self.kappa)

    def __eq__(self, other):
        if not isinstance(other, Foo):
            return False
        return self.alpha == other.alpha and self.kappa == other.kappa

    def __ne__(self, other):
        if not isinstance(other, Foo):
            return False
        return self.alpha != other.alpha and self.kappa != other.kappa

    def __add__(self, other):
        if not isinstance(other, Foo):
            return False
        return Foo('{}{}'.format(self.alpha,other.alpha), self.kappa + other.kappa)
