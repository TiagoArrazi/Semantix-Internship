

class KeyWord:

    @classmethod
    def add(cls, *args):
        return sum(args)


    @classmethod
    def keys_from_dict(cls, **kwargs):
        return [key for key in kwargs.keys()]


    @classmethod
    def values_from_dict(cls, **kwargs):
        return [value for value in kwargs.values()]


    @classmethod
    def get_kwargs(cls, **kwargs):
        return kwargs


    @classmethod
    def add_from_kwargs(cls, **kwargs):
        try:
            return kwargs.get('a') + kwargs.get('b')

        except TypeError as e:
            return 'Missing key argument {}'.format(e)
