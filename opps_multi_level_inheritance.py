class grandfather:
    def v(self):
        print('house')

class dad(grandfather):
    def v1(self):
        print('car')

class son(dad):
    def v2(self):
        print('factory')

s1=son()
s1.v()
s1.v2()
s1.v1()
