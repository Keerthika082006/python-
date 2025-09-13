class grandfather:
    def v(self):
        print('house')
class dad:
    def v1(self):
        print('car')
    def v(self):
        print('home')
class son(dad,grandfather):
    def v2(self):
        print('factory')

s1=son()
s1.v()
s1.v1()
s1.v2()
