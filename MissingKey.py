attributes = {'k1': 'attr1',
              'k2': 'attr2',
              'k3': 'attr3',
              'k4': 'attr4'}


class Foo:

    def __init__(self, attr1='', attr2='', attr3='', attr4=''):
        self.attr1 = attr1
        self.attr2 = attr2
        self.attr3 = attr3
        self.attr4 = attr4


    def __repr__(self):
        return '<Foo {} {} {} {}>'.format(self.attr1,
                                          self.attr2,
                                          self.attr3,
                                          self.attr4)
                                                                
    def __str__(self):
        return '__Foo__'


if __name__ == '__main__':

    data = {'k1':'v1',
            'k2':'v2',
            'k3':'v3'}

    try:
        foo = Foo(data['k1'], data['k2'], data['k3'], data['k4'])
        print(foo.__repr__())

    except KeyError:
        print('Missing keys\n')
        for key in data.keys():
            
            
    
        


