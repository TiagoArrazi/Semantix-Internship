class Foo:

    def __init__(self, alpha):
        self.alpha = alpha

    def __eq__(self, other):
        if not isinstance(other, Foo):
            return False
        return self.alpha == other.alpha
