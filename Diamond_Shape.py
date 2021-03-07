class A:
    def met(self):
        print("This is a method of class A")
class B(A):
    def met(self):
        print("This is a method of class B")

class C(A):
    pass

class D(B,C):  # Taking class acc to given arrangement values(B,C) or (C,B)
    pass

a=A()
b=B()
c=C()
d=D()
d.met()