class A:
    def __init__(self, a):
        self.a = a
        print('a =', a, self.__class__.__name__)

class B(A):
    def __init__(self, a, b):
        self.b = b
        print('b =', b, self.__class__.__name__)
        super().__init__(a)

class C(A):
    def __init__(self, c):
        self.c = c
        print('c =', c, self.__class__.__name__)

class D(B):
    def __init__(self, d):
        self.d = d
        print('d =', d, self.__class__.__name__)
        super().__init__('?', '?')


a1 = A('a')
b1 = B('a', 'b')
c1 = C('c')
d1 = D('d')
